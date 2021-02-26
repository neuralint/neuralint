import numpy as np
import parser_Keras
import nodes_Keras
import grooveParser
import os
#import timeit

def check_Groove():
  grammarName = "DNN-metamodel"
  groovePath = "groove-5_7_4-bin/groove-5_7_4/bin/"
  # FileNameWithoutPath = fileName.split(os.path.sep)[-1]
  grooveOutputFileName = "Model" + "GrooveOut"
  print("Running Model Checker (Groove) ... \n")

  try:
    os.system(
      f'java -jar {groovePath}Generator.jar -f {grooveOutputFileName}.gst -s bfs {grammarName}.gps Model.gst')
  except:
    return f"Error: input file is not valid or not match with selected parser type"

  try:
    result = grooveParser.main(grooveOutputFileName, parserType="keras")
    return result
  except:
    return f"Error: input file is not valid or not match with selected parser type"

def check(model):
    """Prints a string summary of the network.
    Arguments:
        line_length: Total length of printed lines
            (e.g. set this to adapt the display to different
            terminal window sizes).
        positions: Relative or absolute positions of log elements
            in each line. If not provided,
            defaults to `[.33, .55, .67, 1.]`.
        print_fn: Print function to use. Defaults to `print`.
            It will be called on each line of the summary.
            You can set it to a custom function
            in order to capture the string summary.
    Raises:
        ValueError: if `summary()` is called before the model is built.
    """

    if not model.built:
      raise ValueError('This model has not yet been built. '
                     'Build the model first by calling `build()` or calling '
                     '`fit()` with some data, or specify '
                     'an `input_shape` argument in the first layer(s) for '
                     'automatic build.')

    print("Generating model (graph)  ... \n")
    #fileName = 'test'
    #parser_Keras.main(fileName) #sample for old version

    #if model.__class__.__name__ == 'Sequential':
    #print(model.layers[0].get_config()['name'])
    #print(model.__class__.__name__)

    if model.layers[0].get_config()['name'] == 'resnet50':
        input_size = [32, 224, 224, 3]
        output_size = [32, 7, 7, 2048]
    else:
        input_size = list(model.layers[0].get_config()['batch_input_shape'])
        if input_size[0] is None:
           input_size[0] = 32
        output_size = list(model.layers[len(model.layers) - 1].output_shape)
        if output_size[0] is None:
           output_size[0] = 32

    #with open(f"{fileName}.py", "r") as source:
    #  source_code = [line for line in source.readlines()]
    #with open(f"{fileName}.py", "r") as source:
    #  tree = ast.parse(source.read())

    dnn = nodes_Keras.DNN(input_size, output_size)
    ffc = parser_Keras.Parse_Keras_Program(dnn)

    #ffc.visit(tree)

    #start = timeit.default_timer()
    build_summary(model, ffc)

    ffc.add_compile(model)

    program = nodes_Keras.DNN_Program(ffc.DNN, ffc.learner)
    program.gen_graph_nodes_and_edges()
    program.write_graph_node("Model")
    #stop = timeit.default_timer()
    #print('time:', stop - start)

    return (check_Groove())
    #return "Test"

def count_params(weights):
    """Count the total number of scalars composing the weights.
    Arguments:
        weights: An iterable containing the weights on which to compute params
    Returns:
        The total number of scalars composing the weights
    """
    unique_weights = {id(w): w for w in weights}.values()
    weight_shapes = [w.shape.as_list() for w in unique_weights]
    standardized_weight_shapes = [
        [0 if w_i is None else w_i for w_i in w] for w in weight_shapes
    ]
    return int(sum(np.prod(p) for p in standardized_weight_shapes))

def build_summary(model, ffc, line_length=None, positions=None, print_fn=None):
    """Prints a summary of a model.
    Arguments:
        model: Keras model instance.
        line_length: Total length of printed lines
            (e.g. set this to adapt the display to different
            terminal window sizes).
        positions: Relative or absolute positions of log elements in each line.
            If not provided, defaults to `[.33, .55, .67, 1.]`.
        print_fn: Print function to use.
            It will be called on each line of the summary.
            You can set it to a custom function
            in order to capture the string summary.
            It defaults to `print` (prints to stdout).
    """
    if print_fn is None:
        print_fn = print

    if model.__class__.__name__ == 'Sequential':
        sequential_like = True
    elif not model._is_graph_network:
        # We treat subclassed models as a simple sequence of layers, for logging
        # purposes.
        sequential_like = True
    else:
        sequential_like = True
        nodes_by_depth = model._nodes_by_depth.values()
        nodes = []
        #for v in nodes_by_depth:
        #    if (len(v) > 1) or (len(v) == 1 and
        #                        len(nest.flatten(v[0].keras_inputs)) > 1):
                # if the model has multiple nodes
                # or if the nodes have multiple inbound_layers
                # the model is no longer sequential
        #        sequential_like = False
        #        break
        #    nodes += v
        if sequential_like:
            # search for shared layers
            for layer in model.layers:
                flag = False
                for node in layer._inbound_nodes:
                    if node in nodes:
                        if flag:
                            sequential_like = False
                            break
                        else:
                            flag = True
                if not sequential_like:
                    break

    if sequential_like:
        line_length = line_length or 65
        positions = positions or [.45, .85, 1.]
        if positions[-1] <= 1:
            positions = [int(line_length * p) for p in positions]
        # header names for the different log elements
        to_display = ['Layer (type)', 'Output Shape', 'Param #']
    else:
        line_length = line_length or 98
        positions = positions or [.33, .55, .67, 1.]
        if positions[-1] <= 1:
            positions = [int(line_length * p) for p in positions]
        # header names for the different log elements
        to_display = ['Layer (type)', 'Output Shape', 'Param #', 'Connected to']
        relevant_nodes = []
        for v in model._nodes_by_depth.values():
            relevant_nodes += v

    def print_row(fields, positions):
        line = ''
        for i in range(len(fields)):
            if i > 0:
                line = line[:-1] + ' '
            line += str(fields[i])
            line = line[:positions[i]]
            line += ' ' * (positions[i] - len(line))
        print_fn(line)

    #print_fn('Model: "{}"'.format(model.name))
    #print_fn('_' * line_length)
    #print_row(to_display, positions)
    #print_fn('=' * line_length)

    def print_layer_summary(layer):
        """Prints a summary for a single layer.
        Arguments:
            layer: target layer.
        """
        try:
            output_shape = layer.output_shape
        except AttributeError:
            output_shape = 'multiple'
        except RuntimeError:  # output_shape unknown in Eager mode.
            output_shape = '?'
        name = layer.name
        cls_name = layer.__class__.__name__
        fields = [name + ' (' + cls_name + ')', output_shape, layer.count_params()]
        print_row(fields, positions)

    def print_layer_summary_with_connections(layer):
        """Prints a summary for a single layer (including topological connections).
        Arguments:
            layer: target layer.
        """
        try:
            output_shape = layer.output_shape
        except AttributeError:
            output_shape = 'multiple'
        connections = []
        for node in layer._inbound_nodes:
            if relevant_nodes and node not in relevant_nodes:
                # node is not part of the current network
                continue

            for inbound_layer, node_index, tensor_index, _ in node.iterate_inbound():
                connections.append('{}[{}][{}]'.format(inbound_layer.name, node_index,
                                                       tensor_index))

        name = layer.name
        cls_name = layer.__class__.__name__
        if not connections:
            first_connection = ''
        else:
            first_connection = connections[0]
        fields = [
            name + ' (' + cls_name + ')', output_shape,
            layer.count_params(), first_connection
        ]
        print_row(fields, positions)
        if len(connections) > 1:
            for i in range(1, len(connections)):
                fields = ['', '', '', connections[i]]
                print_row(fields, positions)

    #Amin#############################################################################################################
    layers = model.layers
    for i in range(len(layers)):
        if sequential_like:
            if layers[i].get_config()['name'] == 'resnet50':
                build_summary(layers[i], ffc)
            else:
                #print_layer_summary(layers[i])
                ffc.add_Layer(layers[i])
        else:
            print_layer_summary_with_connections(layers[i])
        #if i == len(layers) - 1:
        #    print_fn('=' * line_length)
        #else:
        #    print_fn('_' * line_length)

    if hasattr(model, '_collected_trainable_weights'):
        trainable_count = count_params(model._collected_trainable_weights)
    else:
        trainable_count = count_params(model.trainable_weights)

    non_trainable_count = count_params(model.non_trainable_weights)

    #print_fn('Total params: {:,}'.format(trainable_count + non_trainable_count))
    #print_fn('Trainable params: {:,}'.format(trainable_count))
    #print_fn('Non-trainable params: {:,}'.format(non_trainable_count))
    #print_fn('_' * line_length)