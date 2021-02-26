import ast
from pprint import pprint
from ast import parse, NodeVisitor, literal_eval
from nodes_Keras import *

def main(program_name, input_size=[32, 28, 28, 1], output_size=[32, 10]):
    with open(f"{program_name}.py", "r") as source:
        source_code = [line for line in source.readlines()]
    with open(f"{program_name}.py", "r") as source:
        tree = ast.parse(source.read())
    dnn = DNN(input_size, output_size)
    ffc = Parse_Keras_Program(dnn)
    ffc.visit(tree)
    program = DNN_Program(ffc.DNN, ffc.learner)
    program.gen_graph_nodes_and_edges()
    program.write_graph_node(program_name)
            
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
        return [parse_call(arg.func), parse_params(arg.args, arg.keywords)]
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
        return value + "." + call.attr
    elif isinstance(call, ast.Str):
        return call.s
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

    def visit_Return(self, node):
        if self.func_name != None:
            self.return_ref = node.value

class Parse_Keras_Program(NodeVisitor):

    def __init__(self, dnn):
        self.DNN = dnn
        self.learner = Learner()
        self.batch_size = self.DNN.input_size[0]
        self.learner.set_batch_size(self.batch_size)
        self.model = 'model'
        self.variables = {}
        self.input_layer_name = 'data'
        self.layers_count = 1

    def visit_Assign(self, node):
        asigned_str = parse_arg(node.value)
        asigned_str = asigned_str[0] if isinstance(asigned_str, list) and len(asigned_str) > 0 else asigned_str
        call_target = parse_target(node.targets[0])
        if asigned_str == 'Sequential':
            self.model = call_target
        else:
            self.variables[call_target] = asigned_str   
    
    def add_Layer(self, inLayer):
        config = inLayer.get_config()
        layer_type = inLayer.__class__.__name__
        layer_params = self.DNN.set_params(layer_type, config)
        if self.layers_count == 1:
            layer_params['input_shape'] = list(config['batch_input_shape'])
            if layer_params['input_shape'][0] is None:
                layer_params['input_shape'][0] = 32

        if (layer_type == 'InputLayer'):
            self.layers_count += 1

        #self.change_params_values(layer_params)
        if is_DNN_layer(layer_type):
            layer_params['inputs'] = self.input_layer_name
            #layer_params = self.replace_args(layer_params)
            layer_name = layer_type.lower() + '_' + str(self.layers_count)
            self.DNN.append_layer(layer_name, layer_type, layer_params)
            self.input_layer_name = layer_name
            self.layers_count += 1

    def add_compile(self, model):
        self.DNN.compile()
        #self.change_params_values(call_params)
        if model.__class__.__name__ == 'Sequential':
            loss = Loss(model.loss, 'output')
            loss.set_predictions_layer(self.DNN.get_last_layer_idx())
            self.learner.set_loss(loss)
            opt = Optimizer(model.optimizer.get_config()['name'])
            self.learner.set_optimizer(opt)
            self.learner.set_metric('accuracy')
        else:
            loss = Loss('None', 'output')
            loss.set_predictions_layer(self.DNN.get_last_layer_idx())
            self.learner.set_loss(loss)
            opt = Optimizer('None')
            self.learner.set_optimizer(opt)
        #if 'metrics' in call_params and len(call_params['metrics']) > 0:
            #metric = call_params['metrics'][0]  # Metric(name=call_params['metrics'][0])
            #self.learner.set_metric(metric)
            self.learner.set_metric('accuracy')


    def visit_Call(self, node):
        call_str = parse_call(node.func)
        call_params = parse_params(node.args, node.keywords)
        if call_str == self.model+'.add':
            layer_type = call_params[0][0].split('.')[-1]
            #print(layer_type)
            layer_params = call_params[0][1]
            #print(layer_params)
            self.change_params_values(layer_params)
            #print(layer_params)
            if is_DNN_layer(layer_type): 
                layer_params['inputs'] = self.input_layer_name
                #print(layer_params)
                layer_params = self.replace_args(layer_params)
                #print(layer_params)
                layer_name = layer_type.lower() + '_' + str(self.layers_count)
                self.DNN.append_layer(layer_name, layer_type, layer_params)
                self.input_layer_name = layer_name
                self.layers_count += 1       
        elif call_str == self.model+'.compile':
            self.DNN.compile()
            self.change_params_values(call_params)
            loss = Loss(call_params['loss'], 'output')
            loss.set_predictions_layer(self.DNN.get_last_layer_idx())
            self.learner.set_loss(loss)
            opt = Optimizer(call_params['optimizer'])
            self.learner.set_optimizer(opt)
            if 'metrics' in call_params and len(call_params['metrics'])>0:
                metric = call_params['metrics'][0]#Metric(name=call_params['metrics'][0])
                self.learner.set_metric(metric)
        elif call_str == self.model+'.fit':
            self.change_params_values(call_params)
            epochs = call_params['epochs'] if 'epochs' in call_params else 1
            batch_size = call_params['batch_size'] if 'batch_size' in call_params else self.batch_size
            self.learner.set_vars_init_location(node.func.lineno - 1)
            self.learner.set_train_loop(Train_Loop(node.func.lineno, node.func.lineno))
            self.learner.set_batch_size(batch_size)
            self.learner.set_epochs(epochs)

    def change_params_values(self, params):
        for k, v in params.items():
            if isinstance(v, str) and v in self.variables:
                params[k] = self.variables[v]
    
    def replace_args(self, params):
        def _hashable(v):
            """Determine whether `v` can be hashed."""
            try:
                hash(v)
            except TypeError:
                return False
            return True
        for p_key, p_value in params.items():
            if _hashable(p_value):
                params[p_key] = p_value
            else:
                params[p_key] = None
        return params

if __name__ == "__main__":
    program_name = 'Keras_examples'+os.path.sep+'clean_example'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 20], output_size=[128, 10])
    program_name = 'Keras_examples'+os.path.sep+'deep_CNN'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 224, 224, 3], output_size=[128, 2])
    program_name = 'Keras_examples'+os.path.sep+'deep_CNN_too_much_pooling'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 4098, 4098, 3], output_size=[128, 2])
    program_name = 'Keras_examples'+os.path.sep+'deep_CNN_asymetry_blocks'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 224, 224, 3], output_size=[128, 2])
    program_name = 'Keras_examples'+os.path.sep+'deep_CNN_ineffective_poolings'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 224, 224, 3], output_size=[128, 2])
    program_name = 'Keras_examples'+os.path.sep+'SO_33969059'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 3], output_size=[32, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_34311586'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 2], output_size=[32, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_38584268'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 32, 32, 3], output_size=[32, 10])
    program_name = 'Keras_examples'+os.path.sep+'SO_44322611'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[10, 224, 224, 3], output_size=[10, 2])
    program_name = 'Keras_examples'+os.path.sep+'SO_45378493'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 10, 4], output_size=[128, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_50079585_1'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[16, 150, 150, 3], output_size=[16, 3])
    program_name = 'Keras_examples'+os.path.sep+'SO_50079585_2'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[16, 150, 150, 3], output_size=[16, 3])
    program_name = 'Keras_examples'+os.path.sep+'SO_53119432'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[24, 30, 1], output_size=[24, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_55776436'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 18000, 1], output_size=[32, 6])
    program_name = 'Keras_examples'+os.path.sep+'SO_56103207'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[100, 28, 28, 1], output_size=[100, 4])
    program_name = 'Keras_examples'+os.path.sep+'SO_60566498'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 224, 224, 3], output_size=[32, 3])
    program_name = 'Keras_examples'+os.path.sep+'SO_45120429'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 32, 1], output_size=[32, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_58844149'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 300, 300, 1], output_size=[32, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_51749207'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[8, 600, 1], output_size=[8, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_55731589'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[128, 32, 32, 3], output_size=[128, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_45711636'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[100, 1, 20, 56], output_size=[100, 10])
    program_name = 'Keras_examples'+os.path.sep+'SO_49117607'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 28, 28, 1], output_size=[32, 10])
    program_name = 'Keras_examples'+os.path.sep+'SO_44184091'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 500, 32], output_size=[32, 1])
    program_name = 'Keras_examples'+os.path.sep+'SO_61030068'
    print(f'----------------{program_name}-------------------')
    main(program_name, input_size=[32, 72, 1], output_size=[32, 28])
    