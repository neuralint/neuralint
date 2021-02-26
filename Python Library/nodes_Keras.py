import numpy as np
import os

def fill_in_params(params, args_names):
    new_params = {}
    for key in params.keys():
        if isinstance(key, int):
            new_params[args_names[key]] = params[key]
        else:
            new_params[key] = params[key]
    return new_params

def is_DNN_layer(layer_type):
    supported_layer_types = ['Conv1D', 'Conv2D', 'Conv3D',
                             'MaxPooling1D', 'MaxPooling2D', 'MaxPooling3D',
                             'AveragePooling1D', 'AveragePooling2D', 'AveragePooling3D', 
                             'BatchNormalization', 'Flatten', 'Dense', 'Dropout', 'Activation', 'Reshape']
                             
    lower_layer_type = layer_type.lower()
    if layer_type in supported_layer_types or lower_layer_type in Activation.activations:
        return True
    return False

def is_loss(function):
    losses = Loss.regression_losses + Loss.classification_losses
    if function in losses:
        return True
    return False

def is_optimizer(function):
    optimizers = list(Optimizer.optimizers.values())
    if function in optimizers:
        return True
    return False

class DNN_Program:

    def __init__(self, DNN, learner):
        self.DNN = DNN
        self.learner = learner

    def set_DNN(self, DNN):
        self.DNN = DNN
    
    def set_Learner(self, learner):
        self.learner = learner

    def gen_graph_nodes_and_edges(self):
        self.graph_nodes = ""
        self.graph_edges = ""
        node_counter = 0
        node_id = "n" + str(node_counter)
        self.graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        # DNN_program edges
        self.graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:DNN-program</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        node_counter += 1
        previous_node = node_id
        node_id = "n" + str(node_counter)
        self.graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        # Data Edge
        self.graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        self.graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Data</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        node_counter += 1
        node_id = "n" + str(node_counter)
        self.graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        self.graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
        previous_node, node_id)
        node_counter, added_graph_nodes, added_graph_edges = self.DNN.gen_graph_nodes_and_edges(node_id, node_counter)
        self.graph_nodes += added_graph_nodes
        self.graph_edges += added_graph_edges
        node_counter += 1
        node_id = "n" + str(node_counter)
        self.graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        self.graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                            previous_node, node_id)
        node_counter, added_graph_nodes, added_graph_edges = self.learner.gen_graph_nodes_and_edges(node_id, node_counter)
        self.graph_nodes += added_graph_nodes
        self.graph_edges += added_graph_edges

    def write_graph_node(self, filename):
        filename = filename.split(os.path.sep)[-1]
        #with open(f'Keras_graphs/{filename}.gst', 'w') as f:
        with open(f'{filename}.gst', 'w') as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<gxl xmlns=\"http://www.gupro.de/GXL/gxl-1.0.dtd\">\n")
            f.write("\t<graph role=\"graph\" edgeids=\"false\" edgemode=\"directed\" id=\"start1\">\n")
            f.write(self.graph_nodes)
            f.write(self.graph_edges)
            # Finalizing the gst file
            f.write("\t</graph>\n</gxl>")

class Learner:

    def __init__(self):
        self.metric = 'mean_absolute_error'
        self.batch_size = 32
        self.epochs = 100

    def set_vars_init_location(self, vars_init_location):
        self.vars_init_location = vars_init_location

    def set_train_loop(self, train_loop):
        self.train_loop = train_loop

    def set_loss(self, loss):
        self.loss = loss
    
    def set_optimizer(self, optimizer):
        self.optimizer = optimizer
    
    def set_metric(self, metric):
        self.metric = metric
    
    def set_batch_size(self, batch_size):
        self.batch_size = batch_size
    
    def set_epochs(self, epochs):
        self.epochs = epochs
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Main
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Learner</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        if hasattr(self, 'train_loop'):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:loop_line_start = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    node_id, node_id, self.train_loop.start_loc)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:loop_line_end = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    node_id, node_id, self.train_loop.end_loc)
        if hasattr(self, 'vars_init_location'):
            is_there_global_init = True if self.vars_init_location!=None else False
            if is_there_global_init:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:global_initializer = bool:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    node_id, node_id, str(is_there_global_init).lower())
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:location_of_initializer = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.vars_init_location)
        #Loss
        node_counter += 1
        previous_node = node_id
        node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Loss</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.loss.name)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:predictions = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.loss.predictions_layer)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:input_type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.loss.input_type)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:problem_type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.loss.problem_type)
        #Optimizer
        node_counter += 1
        node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Optimizer</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.optimizer.name)
        #graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:learning_rate = real:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
        #        node_id, node_id, self.optimizer.learning_rate)
        #graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:initializer = bool:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
        #        node_id, node_id, self.optimizer.initializer)
        #Hyperaparameters
        node_counter += 1
        node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Hyperparameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:batchSize = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.batch_size)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:epochCount = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.epochs)
        #Metric
        node_counter += 1
        node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Metric</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.metric)
        return node_counter, graph_nodes, graph_edges
 
class Train_Loop:

    def __init__(self, start_loc, end_loc):
        self.start_loc = start_loc
        self.end_loc = end_loc

class Optimizer:
    optimizers = {'sgd':'SGD', 'rmsprop':'RMSprop', 
                  'adagrad':'Adagrad', 'adam':'Adam', 'adadelta':'Adadelta'}
    params = ['learning_rate']

    def __init__(self, name, learning_rate=None, additional_params=None):
        self.name = self.clean(name)
        self.learning_rate = learning_rate
        self.additional_params = additional_params
    
    def clean(self, name):
        for short_name, long_name in Optimizer.optimizers.items():
            if name == long_name:
                return short_name
 
class Loss:

    regression_losses = ['hinge', 'huber_loss', 'mean_squared_error', 'mean_absolute_error', 'mae']
    classification_losses = ['binary_crossentropy', 'categorical_crossentropy', 'sparse_categorical_crossentropy']
    params = {loss:['labels', 'predictions'] for loss in regression_losses}
    params.update({loss:['labels', 'logits'] if loss !='log_loss' else ['labels', 'predictions'] for loss in classification_losses})

    def __init__(self, name, predictions):
        self.name = name
        self.predictions = predictions
        self.infer_problem_type()
        self.infer_input_type()
        
    def set_predictions_layer(self, predictions_layer):
        self.predictions_layer = predictions_layer

    def infer_input_type(self):
        if self.problem_type == 'regression':
            self.input_type = 'pre_activation'
        elif self.problem_type == 'classification':
            self.input_type = 'post_activation'
        else:
            self.input_type = 'None'
            #if Loss.params[self.name][1] == 'predictions':
                #self.input_type = 'post_activation'
            #elif Loss.params[self.name][1] == 'logits':
                #self.input_type = 'pre_activation'
    
    def infer_problem_type(self):
        if self.name in Loss.regression_losses:
            self.problem_type = 'regression'
        elif self.name in Loss.classification_losses:
            self.problem_type = 'classification'
        else:
            self.problem_type = 'None'

class Metric:

    def __init__(self, name):
        self.name = name
        self.infer_problem_type()
        self.infer_input_type()

    def infer_problem_type(self):
        pass
    
    def infer_input_type(self):
        pass

class DNN:

    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.layers = []
        self.convs_count = 0
        self.pools_count = 0 
    
    def append_layer(self, layer_name, layer_type, params):
        if layer_type in ['Conv1D', 'Conv2D', 'Conv3D']:
            params_dict = fill_in_params(params, args_names=Convolutional.params)
            conv = Convolutional(layer_name, params_dict['inputs'], params_dict) 
            self.convs_count += 1
            self.layers.append(conv)  
        elif layer_type in ['MaxPooling1D', 'MaxPooling2D', 'MaxPooling3D',
                            'AveragePooling1D', 'AveragePooling2D', 'AveragePooling3D',
                            'MaxPool1D', 'MaxPool2D', 'MaxPool3D']:
            params_dict = fill_in_params(params, args_names=Pooling.params)
            pool = Pooling(layer_name, params_dict['inputs'], params_dict)
            self.pools_count += 1
            self.layers.append(pool)  
        elif layer_type == 'Flatten':
            params_dict = fill_in_params(params, args_names=Flatten.params)
            flat = Flatten(layer_name, params_dict['inputs'])
            self.layers.append(flat)  
        elif layer_type == 'Reshape':
            params_dict = fill_in_params(params, args_names=Reshape.params)
            reshape = Reshape(layer_name, params_dict['inputs'], params_dict['target_shape'])
            self.layers.append(reshape)  
        elif layer_type == 'Dense':
            params_dict = fill_in_params(params, args_names=Dense.params)
            dense = Dense(layer_name, params_dict['inputs'], params_dict)
            self.layers.append(dense)  
        elif layer_type == 'Dropout':
            params_dict = fill_in_params(params, args_names=Dropout.params)
            dropout = Dropout(layer_name, params_dict['inputs'], params_dict['rate'])
            self.layers.append(dropout)  
        elif layer_type == 'BatchNormalization':
            params_dict = fill_in_params(params, args_names=Batchnorm.params)
            batchnorm = Batchnorm(layer_name, params_dict['inputs'])
            self.layers.append(batchnorm)  
        elif layer_type == 'Activation':
            layer_type = params[0]
            inputs = params['inputs']
            activation = Activation(layer_name, inputs, layer_type)
            self.layers.append(activation)
        elif layer_type.lower() in Activation.activations:
            params_dict = fill_in_params(params, args_names=Activation.params)
            inputs = params_dict['inputs']
            activation = Activation(layer_name, inputs, layer_type)
            self.layers.append(activation)  

    def update_layers_name(self, old_name, new_name):
        for layer in self.layers:
            if layer.name == old_name:
                layer.name = new_name

    def compile(self):
        def _layer_idx(layer_name, connected_layers):
            for layer_idx in range(len(connected_layers)):
                if connected_layers[layer_idx].name == layer_name:
                    return layer_idx
        connected_layers = []
        input_layer_name = self.layers[0].input_layer_name
        input_size = self.input_size
        inp_layer_names = [layer.input_layer_name for layer in self.layers]
        reversed_inp_layer_names = list(reversed(inp_layer_names))
        idx = 0
        while idx != len(reversed_inp_layer_names) - 1:
            idx = (len(reversed_inp_layer_names)-1) - reversed_inp_layer_names.index(input_layer_name)
            self.layers[idx].set_input_size(input_size)
            input_size = self.layers[idx].output_size
            input_layer_name = self.layers[idx].name
            connected_layers.append(self.layers[idx])
        layers_to_add = {}
        for layer_idx in range(len(connected_layers)):
            layer = connected_layers[layer_idx]
            ##################Amin
            #print(layer.name)
            if isinstance(layer, Convolutional) or isinstance(layer, Dense):
                if layer.activation:
                    activation_layer = Activation(f'act_{layer.name}', layer.name, layer.activation)
                    activation_layer.set_input_size(layer.output_size)
                    layers_to_add[layer.name] = activation_layer       
        for layer_name, layer_to_add in layers_to_add.items():
            layer_idx = _layer_idx(layer_name, connected_layers)
            connected_layers.insert(layer_idx+1, layer_to_add)
        self.layers = connected_layers

    def get_last_layer_idx(self):
        return len(self.layers)

    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Main
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Architecture</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:hiddenLayerCount = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.layers))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:ConvCount = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.convs_count)  
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:PoolCount = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.pools_count)
        #Input Layer
        node_counter += 1
        previous_node = node_id
        node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        layer_counter = 0
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>starts</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:InputLayer</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:No = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, layer_counter)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:dim1 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.input_size[1])
        if len(self.input_size) == 3:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:channels = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.input_size[2])
        elif len(self.input_size) == 4:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:dim2 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.input_size[2])
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:channels = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.input_size[3])
        elif len(self.input_size) == 5:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:dim2 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.input_size[2])
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:dim3 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.input_size[3])
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:channels = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, self.input_size[4])
        # Hidden Layers
        for layer_idx in range(len(self.layers)):
            layer = self.layers[layer_idx]
            layer_counter += 1
            node_counter += 1
            previous_node = node_id
            node_id = "n" + str(node_counter)
            graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
            if layer_idx == 0:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>followed-by</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                        previous_node, node_id)
            else:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>next</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    previous_node, node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:No = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, layer_counter)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Layer</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id)
            if layer_idx == len(self.layers) - 1:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>flag:output</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    node_id, node_id)
            node_counter, added_graph_nodes, added_graph_edges = layer.gen_graph_nodes_and_edges(node_id, node_counter)
            graph_nodes += added_graph_nodes
            graph_edges += added_graph_edges 
        #Labels Layer
        node_counter += 1
        previous_node = node_id
        node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(node_id)
        layer_counter = 0
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>ends</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            previous_node, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Labels</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:size = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, self.output_size[1])
        return node_counter, graph_nodes, graph_edges
    
    def __str__(self):
        s = ''
        for layer in self.layers:
            s += f'{layer.input_layer_name}== {layer.__class__.__name__} ==> {layer.name}'
            if hasattr(layer, "output_size"):
                s += f'|({layer.input_size} ==> {layer.output_size})'
            s += ' \n'
        return s
    #Amin
    def set_params(self, layer_type, config):
        params = {}
        if layer_type in ['Conv1D', 'Conv2D', 'Conv3D']:
            params = {
                'filters' : config['filters'],
                'kernel_size' : int(config['kernel_size'][0]) if (len(config['kernel_size']) == 1) else config['kernel_size'],
                'activation' : config['activation'],
                'padding' : config['padding'],
                'use_bias': config['use_bias'],
                'inputs' : ''
            }
        elif layer_type in ['MaxPooling1D', 'MaxPooling2D', 'MaxPooling3D',
                            'AveragePooling1D', 'AveragePooling2D', 'AveragePooling3D',
                            'MaxPool1D', 'MaxPool2D', 'MaxPool3D']:
            params = {
                'pool_size' : int(config['pool_size'][0]) if (len(config['pool_size']) == 1) else config['pool_size'],
                'strides' : int(config['strides'][0]) if (len(config['strides']) == 1) else config['strides'],
                'data_format' : config['data_format'],
                'inputs' : ''
            }
        elif layer_type == 'Flatten':
            params = {
                'inputs' : ''
            }
        elif layer_type == 'Reshape':
            params = {
                'target_shape': config['target_shape'],
                'inputs' : ''
            }
        elif layer_type == 'Dense':
            params = {
                'units' : config['units'],
                'activation' : config['activation'],
                'kernel_constraint' : None,
                'inputs': ''
            }
        elif layer_type == 'Dropout':
            params = {
                'rate' : config['rate'],
                'inputs': ''
            }
        elif layer_type == 'BatchNormalization':
            params = {
                'inputs' : ''
            }
        elif layer_type == 'Activation':
            params = {
                0 : config['activation'],
                'inputs': ''
            }
        elif layer_type.lower() in Activation.activations:
            params = {
                'inputs': ''
            }
        return params

class Processing_Layer:
    
    def __init__(self, name, input_layer_name):
        self.name = name
        self.input_layer_name = input_layer_name

class Learning_Layer(Processing_Layer):
    
    def __init__(self, name, input_layer_name):
        super(Learning_Layer, self).__init__(name, input_layer_name)
        
class Convolutional(Learning_Layer):
    params = ['filters', 'kernel_size', 'strides', 'padding', 'inputs']

    def __init__(self, name, input_layer_name, params):
        super(Convolutional, self).__init__(name, input_layer_name)
        self.filters = params['filters'] if 'filters' in params else None
        self.set_kernel_size(params)
        self.set_strides(params)
        self.padding = params['padding'] if 'padding' in params else 'valid'
        self.activation = params['activation'] if 'activation' in params else None
        if self.activation == 'linear':
            self.activation = None
        self.use_bias = params['use_bias'] if 'use_bias' in params else True
        self.W_init = params['kernel_initializer'] if 'kernel_initializer' in params else 'glorot_uniform'
        self.b_init = params['bias_initializer'] if 'bias_initializer' in params else 'zeros'
        self.W_cons = params['kernel_constraint'] if 'kernel_constraint' in params else None
        self.b_cons = params['bias_constraint'] if 'bias_constraint' in params else None
        self.W_reg = params['kernel_regularizer'] if 'kernel_regularizer' in params else None
        self.b_reg = params['bias_regularizer'] if 'bias_regularizer' in params else None
        self.clean_strings_names()
    
    def clean_strings_names(self):
        if self.activation:
            self.activation = self.activation.split('.')[-1]
        if self.W_init:
            self.W_init = self.W_init.split('.')[-1]
            if self.W_init in ['zeros', 'ones']:
                self.W_init = 'constant'
        if self.b_init:
            self.b_init = self.b_init.split('.')[-1]
        if self.W_cons:
            self.W_cons = self.W_cons.split('.')[-1]
        if self.b_cons:
            self.b_cons = self.b_cons.split('.')[-1]
        if self.W_reg:
            self.W_reg = self.W_reg.split('.')[-1]
        if self.b_reg:
            self.b_reg = self.b_reg.split('.')[-1]

    def set_kernel_size(self, params):
        kernel_size = params['kernel_size'] if 'kernel_size' in params else None
        if isinstance(kernel_size, list):
            self.kernel_size = kernel_size
        elif isinstance(kernel_size, tuple):
            self.kernel_size = [kernel_size[0], kernel_size[1]]    
        else:
            self.kernel_size = [kernel_size, kernel_size]

    def set_strides(self, params):
        strides = params['strides'] if 'strides' in params else (1, 1)
        if isinstance(strides, list):
            self.strides = strides
        elif isinstance(strides, tuple):
            self.strides = [strides[0], strides[1]]
        else:
            self.strides = [strides, strides]

    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        if len(self.input_size) == 4:
            batch_size, in_height, in_width, in_depth = self.input_size
            if self.padding == 'valid':
                out_height = (in_height - self.kernel_size[0]) / self.strides[0] + 1
                out_width = (in_width - self.kernel_size[1]) / self.strides[1] + 1
            elif self.padding == 'same':
                out_height = (in_height - 1) / self.strides[0] + 1
                out_width = (in_width - 1) / self.strides[1] + 1
            elif self.padding == 'full':
                out_height = (in_height + self.kernel_size[0] - 2) / self.strides[0] + 1
                out_width = (in_width + self.kernel_size[1] - 2) / self.strides[1] + 1
            return [batch_size, int(out_height), int(out_width), self.filters]
        elif len(self.input_size) == 3:
            batch_size, in_steps, in_depth = self.input_size
            if self.padding == 'valid':
                out_steps = (in_steps - self.kernel_size[0]) / self.strides[0] + 1
            elif self.padding == 'same':
                out_steps = (in_steps - 1) / self.strides[0] + 1
            elif self.padding == 'full':
                out_steps = (in_steps + self.kernel_size[0] - 2) / self.strides[0] + 1
            return [batch_size, int(out_steps), self.filters]
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.name.split('_')[0])
        
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:filters = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.filters)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:strides_dim1 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.strides[0])
        if 'conv2d' in self.name or 'conv3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:strides_dim2 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.strides[1])
        if 'conv3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:strides_dim3 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.strides[2])
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:kernel_dim1 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.kernel_size[0])
        if 'conv2d' in self.name or 'conv3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:kernel_dim2 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.kernel_size[1])
        if 'conv3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:kernel_dim3 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.kernel_size[2])
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:padding = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.padding)
        #additional Attributes
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Weights</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:initializer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.W_init)
        if self.W_cons:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:regularizer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.W_cons)
        if self.W_reg:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:constraint = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.W_reg)
        if self.use_bias:
            node_counter += 1
            next_node_id = "n" + str(node_counter)
            graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Bias</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:initializer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.b_init)
            if self.b_cons:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:regularizer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.b_cons)
            if self.b_reg:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:constraint = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.b_reg)
        return node_counter, graph_nodes, graph_edges

class Dense(Learning_Layer):
    params = ['units', 'activation', 'use_bias', 'kernel_initializer', 'bias_initializer', 'kernel_regularizer', 'bias_regularizer','inputs']
    
    def __init__(self, name, input_layer_name, params):
        super(Dense, self).__init__(name, input_layer_name)
        self.units = params['units'] if 'units' in params else None
        self.activation = params['activation'] if 'activation' in params else None
        if self.activation == 'linear':
            self.activation = None
        self.use_bias = params['use_bias'] if 'use_bias' in params else True
        self.W_init = params['kernel_initializer'] if 'kernel_initializer' in params else 'glorot_uniform'
        self.b_init = params['bias_initializer'] if 'bias_initializer' in params else 'zeros'
        self.W_cons = params['kernel_constraint'] if 'kernel_constraint' in params else None
        self.b_cons = params['bias_constraint'] if 'bias_constraint' in params else None
        self.W_reg = params['kernel_regularizer'] if 'kernel_regularizer' in params else None
        self.b_reg = params['bias_regularizer'] if 'bias_regularizer' in params else None
        self.clean_strings_names()

    def clean_strings_names(self):
        if self.activation:
            self.activation = self.activation.split('.')[-1]
        if self.W_init:
            self.W_init = self.W_init.split('.')[-1]
            if self.W_init in ['zeros', 'ones']:
                self.W_init = 'constant'
        if self.b_init:
            self.b_init = self.b_init.split('.')[-1]
        if self.W_cons:
            self.W_cons = self.W_cons.split('.')[-1]
        if self.b_cons:
            self.b_cons = self.b_cons.split('.')[-1]
        if self.W_reg:
            self.W_reg = self.W_reg.split('.')[-1]
        if self.b_reg:
            self.b_reg = self.b_reg.split('.')[-1]
            
    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        batch_size = self.input_size[0]
        return [batch_size, self.units]
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, 'dense')
        #additional Attributes
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Weights</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:initializer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.W_init)
        if self.W_cons:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:regularizer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.W_cons)
        if self.W_reg:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:constraint = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.W_reg)
        if self.use_bias:
            node_counter += 1
            next_node_id = "n" + str(node_counter)
            graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Bias</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:initializer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.b_init)
            if self.b_cons:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:regularizer = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.b_cons)
            if self.b_reg:
                graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:constraint = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.b_reg)
        return node_counter, graph_nodes, graph_edges

class Pooling(Processing_Layer):
    params = ['pool_size', 'strides', 'padding', 'inputs']
    def __init__(self, name, input_layer_name, params):
        super(Pooling, self).__init__(name, input_layer_name)
        self.set_pool_size(params)
        self.set_strides(params)
        self.padding = params['padding'] if 'padding' in params else 'valid'

    def set_pool_size(self, params):
        pool_size = params['pool_size'] if 'pool_size' in params else [2, 2]
        if isinstance(pool_size, list):
            self.pool_size = pool_size
        elif isinstance(pool_size, tuple):
            self.pool_size = [pool_size[0], pool_size[1]]    
        else:
            self.pool_size = [pool_size, pool_size]

    def set_strides(self, params):
        strides = params['strides'] if 'strides' in params else None
        if strides is None or strides == 'None':
            strides = self.pool_size
        if isinstance(strides, list):
            self.strides = strides
        elif isinstance(strides, tuple):
            self.strides = [strides[0], strides[1]]    
        else:
            self.strides = [strides, strides]

    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        if len(self.input_size) == 4:
            batch_size, in_height, in_width, in_depth = self.input_size
            if self.padding == 'valid':
                out_height = (in_height - self.pool_size[0]) / self.strides[0] + 1
                out_width = (in_width - self.pool_size[1]) / self.strides[1] + 1
            elif self.padding == 'same':
                out_height = (in_height - 1) / self.strides[0] + 1
                out_width = (in_width - 1) / self.strides[1] + 1
            elif self.padding == 'full':
                out_height = (in_height + self.pool_size[0] - 2) / self.strides[0] + 1
                out_width = (in_width + self.pool_size[1] - 2) / self.strides[1] + 1
            return [batch_size, int(out_height), int(out_width), in_depth]
        elif len(self.input_size) == 3:
            batch_size, in_steps, in_depth = self.input_size
            if self.padding == 'valid':
                out_steps = (in_steps - self.pool_size[0]) / self.strides[0] + 1
            elif self.padding == 'same':
                out_steps = (in_steps - 1) / self.strides[0] + 1
            elif self.padding == 'full':
                out_steps = (in_steps + self.pool_size[0] - 2) / self.strides[0] + 1
            return [batch_size, int(out_steps), in_depth]
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.name.split('_')[0])
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:pool_dim1 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.pool_size[0])
        if '2d' in self.name or '3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:pool_dim2 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.pool_size[1])
        if '3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:pool_dim3 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                    next_node_id, next_node_id, self.pool_size[2])
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:strides_dim1 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.strides[0])
        if '2d' in self.name or '3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:strides_dim2 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.strides[1])
        if '3d' in self.name:
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:strides_dim3 = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.strides[2])
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:padding = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.padding)
        return node_counter, graph_nodes, graph_edges

class Dropout(Processing_Layer):
    params = ['rate', 'inputs']
    
    def __init__(self, name, input_layer_name, rate=0.5):
        super(Dropout, self).__init__(name, input_layer_name)
        self.rate = rate
        
    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        return self.input_size
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, 'dropout')
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:dropoutRate = real:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.rate)
        return node_counter, graph_nodes, graph_edges

class Batchnorm(Processing_Layer):
    params = ['inputs']
    
    def __init__(self, name, input_layer_name):
        super(Batchnorm, self).__init__(name, input_layer_name)
        
    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        return self.input_size
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, 'batch_norm')
        return node_counter, graph_nodes, graph_edges

class Reshape(Processing_Layer):
    params = ['target_shape', 'inputs']
    def __init__(self, name, input_layer_name, output_shape):
        super(Reshape, self).__init__(name, input_layer_name)
        self.output_shape = output_shape
        
    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        output_shape = self.output_shape
        if -1 in output_shape:
            full_dims = np.prod(np.array(self.input_size))
            idx = output_shape.index(-1)
            output_shape[idx] = int(full_dims/np.prod(np.absolute(np.array(output_shape))))
            if np.prod(np.array(output_shape)) != full_dims:
                raise ValueError('The output shapes are not valid')
        return output_shape
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, 'reshape')
        return node_counter, graph_nodes, graph_edges
    
class Flatten(Processing_Layer):
    params = ['inputs']
    def __init__(self, name, input_layer_name):
        super(Flatten, self).__init__(name, input_layer_name)
        
    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        batch_size = self.input_size[0]
        return [batch_size, int(np.prod(self.input_size[1:]))]

    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, 'flatten')
        return node_counter, graph_nodes, graph_edges

class Activation(Processing_Layer):
    activations = ['elu', 'relu', 'selu', 'relu6', 'leakyrelu', 'tanh', 'sigmoid', 'softmax', 'linear']
    params  = ['inputs']

    def __init__(self, name, input_layer_name, activation):
        super(Activation, self).__init__(name, input_layer_name)
        self.activation = activation if activation else 'linear'
        self.non_linear = self.check_non_linearity()

    def check_non_linearity(self):
        if self.activation in ['identity']:
            return False
        return True

    def set_input_size(self, input_size):
        self.input_size = input_size
        self.output_size = self.infer_output_size()

    def infer_output_size(self):
        return self.input_size
    
    def gen_graph_nodes_and_edges(self, node_id, node_counter):
        graph_nodes = ""
        graph_edges = ""
        #Layer
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.input_size))
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dims = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
            node_id, node_id, len(self.output_size))
        for i in range(len(self.input_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:in_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.input_size[i])
        for i in range(len(self.output_size)):
            graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:out_dim{} = int:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, node_id, i, self.output_size[i])
        node_counter += 1
        next_node_id = "n" + str(node_counter)
        graph_nodes += "\t\t<node id=\"{}\"/>\n".format(next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>has-a</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>type:Parameters</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:type = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, 'activator')
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:activation = string:\"{}\"</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, self.activation)
        graph_edges += "\t\t<edge from=\"{}\" to=\"{}\">\n\t\t\t<attr name=\"label\">\n\t\t\t\t<string>let:nonLinear = bool:{}</string>\n\t\t\t</attr>\n\t\t</edge>\n".format(
                next_node_id, next_node_id, str(self.non_linear).lower())
        return node_counter, graph_nodes, graph_edges