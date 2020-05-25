import ast
from pprint import pprint
from ast import parse, NodeVisitor, literal_eval
from nodes_TF import *

def main(program_name, input_size=[32, 28, 28, 1], output_size=[32, 10]):
    with open(f"{program_name}.py", "r") as source:
        source_code = [line for line in source.readlines()]
    with open(f"{program_name}.py", "r") as source:
        tree = ast.parse(source.read())
    ffc = Find_Function_Calls()
    ffc.visit(tree)
    model = DNN(input_size, output_size)
    train_op_ref, opt, loss = parse_assigns_with_call(model, ffc.assigns_with_call, tree)
    model.compile()
    loss.set_predictions_layer(model.get_last_layer_idx(loss.predictions))
    learner = Learner()
    learner.set_loss(loss)
    learner.set_optimizer(opt)
    learner.set_batch_size(input_size[0])
    fc = Find_Loops_And_Runs(source_code, train_op_ref)
    fc.visit(tree)
    learner.set_vars_init_location(fc.init_line)
    if len(fc.loops) > 0:
        main_loop = parse_main_loop(fc.loops, fc.train_line)
        train_loop = Train_Loop(main_loop['start'], main_loop['end'])
    else:
        train_loop = Train_Loop(0, 0)
    learner.set_train_loop(train_loop)
    program = DNN_Program(model, learner)
    program.gen_graph_nodes_and_edges()
    program.write_graph_node(program_name)

def parse_assigns_with_call(model, assigns_with_call, ast):
    opt_ref, loss_ref = '', ''
    for call_target, (call_str, call_params) in assigns_with_call.items():
        if is_optimizer(call_str.split('.')[-1]):
            opt_ref = call_target
            opt = Optimizer(name=call_str.split('.')[-1])
        if call_str == f'{opt_ref}.minimize':
            loss_ref = list(call_params.values())[0]
            labels, logits = list(assigns_with_call[loss_ref][1].values())
            loss_func = Loss(assigns_with_call[loss_ref][0].split('.')[-1], logits)
            train_op_ref = call_target
            while logits in assigns_with_call:
                func_name, params = assigns_with_call[logits]
                layer_type = func_name.split('.')[-1]
                if is_DNN_layer(layer_type):
                    model.prepend_layer(logits, layer_type, params)
                    logits = model.layers[0].input_layer_name
                else:
                    args = list(params.values())
                    fl = Find_Layers(func_name, args)
                    fl.visit(ast)
                    for layer_name, layer_type, params in reversed(fl.layers_data):
                        #print(layer_name, layer_type, params)
                        model.prepend_layer(layer_name, layer_type, params)
                    model.update_layers_name(fl.return_ref.id, logits)
                    logits = model.layers[0].input_layer_name
    return train_op_ref, opt, loss_func

def parse_main_loop(loops, train_line):
    loops = sorted(loops, key=lambda kv: kv['start']+kv['end'], reverse=True)
    for loop in loops:
        if train_line in range(loop['start'],loop['end']):
            return loop
            
def parse_arg(arg):
    if isinstance(arg, ast.Str):
        return arg.s
    elif isinstance(arg, ast.Name):
        value = None if arg.id == "None" else arg.id
        return value
    elif isinstance(arg, ast.NameConstant):
        return arg.value
    elif isinstance(arg, ast.Num):
        return arg.n
    elif isinstance(arg, ast.List):
        arg_list = []
        for elt in arg.elts:
            arg_list.append(parse_arg(elt))
        return arg_list
    elif isinstance(arg, ast.Tuple):
        arg_list = []
        for elt in arg.elts:
            arg_list.append(parse_arg(elt))
        return tuple(arg_list)
    elif isinstance(arg, ast.Attribute):
        value = parse_arg(arg.value)
        return value + "." + arg.attr
        #return (str(arg.value.attr) + "." + str(arg.attr))
    elif isinstance(arg, ast.Call):
        return parse_call(arg.func)
    elif isinstance(arg, ast.UnaryOp):
        if isinstance(arg.op, ast.USub):
            return -1 * arg.operand.n
    else:
        return arg 

def parse_call(call):
    if isinstance(call, ast.Name):
        value = None if call.id == "None" else call.id
        return value
    elif isinstance(call, ast.Attribute):
        value = parse_call(call.value)
        if isinstance(value, ast.BinOp):
            print(value.left.id, value.op, value.right.n)
        return value + "." + call.attr
    else:
        return call 

def parse_target(arg):
    if isinstance(arg, ast.Name):
        value = None if arg.id == "None" else arg.id
        return value
    elif isinstance(arg, ast.Tuple):
        arg_list = []
        for elt in arg.elts:
            arg_list.append(parse_target(elt))
        return ','.join(arg_list)
    elif isinstance(arg, ast.Attribute):
        return (str(arg.value.id) + "." + str(arg.attr))
    else:
        return arg

def parse_params(args, keywords):
    params = {}
    for arg_idx in range(len(args)):
        arg = args[arg_idx]
        params[arg_idx] = parse_arg(arg)
    for keyword in keywords:
        params[keyword.arg] = parse_arg(keyword.value)
    return params

def compute_interval(node):
    min_lineno = node.lineno
    max_lineno = node.lineno
    for node in ast.walk(node):
        if hasattr(node, "lineno"):
            min_lineno = min(min_lineno, node.lineno)
            max_lineno = max(max_lineno, node.lineno)
    return (min_lineno, max_lineno + 1)

class Find_Layers(NodeVisitor):

    def __init__(self, func_name, args):
        self.func_name = func_name
        self.return_ref = None
        self.args = args
        self.args_matches = {}
        self.layers_data = []
    
    def visit_FunctionDef(self, node):
        if self.func_name == None:
            self.generic_visit(node)
        else:
            if node.name == self.func_name:
                for i in range(len(node.args.args)):
                    param = node.args.args[i].arg
                    self.args_matches[parse_arg(param)] = self.args[i]
                # visit the children
                self.generic_visit(node)

    def replace_args(self, params):
        def _hashable(v):
            """Determine whether `v` can be hashed."""
            try:
                hash(v)
            except TypeError:
                return False
            return True
        for p_key, p_value in params.items():
            if _hashable(p_value) and p_value in self.args_matches:
                params[p_key] = self.args_matches[p_value]
        return params

    def visit_Assign(self, node):
        if isinstance(node.value, ast.Call):
            layer_type = (node.value.func.attr).lower()
            layer_name = parse_target(node.targets[0]).lower()
            if is_DNN_layer(layer_type): 
                args = node.value.args
                kwargs = node.value.keywords
                params = parse_params(args, kwargs)
                params = self.replace_args(params)
                self.layers_data.append((layer_name, layer_type, params))

    def visit_Return(self, node):
        if self.func_name != None:
            self.return_ref = node.value

class Find_Function_Calls(NodeVisitor):

    def __init__(self):
        self.assigns_with_call = {}

    def visit_Assign(self, node):
        if isinstance(node.value, ast.Call):
            call_str = parse_call(node.value.func)
            call_target = parse_target(node.targets[0])
            call_params = parse_params(node.value.args, node.value.keywords)
            self.assigns_with_call[call_target] = (call_str, call_params)

class Find_Loops_And_Runs(NodeVisitor):

    def __init__(self, source_code, train_op):
        self.source_code = source_code
        self.train_op = train_op
        self.sess_ref = ''
        self.train_line = None
        self.init_line = None
        self.loops = []

    def visit_Call(self, node):
        call_str = parse_call(node.func)
        if len(call_str.split('.'))==2 and 'Session'==call_str.split('.')[1]:
            if 'as' in self.source_code[node.func.lineno-1]:
                self.sess_ref = self.source_code[node.func.lineno-1].split('as')[1].replace(':','').strip()
            elif '=' in self.source_code[node.func.lineno-1]:
                self.sess_ref = self.source_code[node.func.lineno-1].split('=')[0].strip()
        run_call = self.sess_ref + '.run'
        if call_str == run_call:
            vars = parse_arg(node.args[0])
            if isinstance(vars, list) and 'tf.global_variables_initializer' in vars:
                self.init_line = node.func.lineno
            elif vars == 'tf.global_variables_initializer':
                self.init_line = node.func.lineno
            if isinstance(vars, list) and self.train_op in vars:
                self.train_line = node.func.lineno
            elif self.train_op == vars:
                self.train_line = node.func.lineno
    
    def visit_For(self, node):
        start, end = compute_interval(node)
        self.loops.append({'start':start, 'end':end})
        # visit the children
        self.generic_visit(node)
    
    def visit_While(self, node):
        start, end = compute_interval(node)
        self.loops.append({'start':start, 'end':end})
        # visit the children
        self.generic_visit(node)

if __name__ == "__main__":
    program_name = 'TF_lenet_disconnected_pooling_layers'
    main(program_name, input_size=[32, 28, 28, 1], output_size=[32, 10])