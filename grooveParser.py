import xml.etree.ElementTree as ET


def tagEditor(tag):
    return tag.replace("{http://www.gupro.de/GXL/gxl-1.0.dtd}","")

def checkErrorCode(faultNode, flagsName):
    for key in flagsName.keys():
        if key == faultNode:
            return flagsName.get(faultNode)
        else:
            return None

def preprocessing(learnerNodeName,flagsName, edgeName, faultName):
    # synchronising fualts and flags
    notErrorcodes = []
    for key in flagsName.keys():
        if key not in faultName:
            notErrorcodes.append(key)
    for item in notErrorcodes:
        del flagsName[item]

    # synchronising edges and faults
    notErrorEdges = []
    for item in edgeName:
        if item.get("to") not in flagsName.keys() or item.get("from")==learnerNodeName:
            notErrorEdges.append(item)
    for item in notErrorEdges:
        edgeName.remove(item)

def faultCodeTranslator(fault):
    if fault == "f001":
        return "A processing layer that operates on a N-dimensional tensors, should receive a valid input tensor with exactly N-dimensional shape(Missing reshape)."
    elif fault == "f002":
        return "Max-pooling is the preferred down-sampling strategy(lack of pooling)."
    elif fault == "f003":
        return "Multiple and redundant connected activations are not allowed."
    elif fault == "f004":
        return "The initialization of weights should not be constant to break the symmetry between neurons."
    elif fault == "f005":
        return "A learning layer should no longer include a bias when it is followed by batchnorm."
    elif fault == "f006":
        return "Batchnorm layer should be before the dropout."
    elif fault == "f007":
        return "The learnable parameters should be totally initialized once at the beginning of the training(multiple inits)"
    elif fault == "f008":
        return "A last layer activation is required to transform the logits into probabilities for classification problem(missing softmax)."
    elif fault == "f009":
        return "Activations for learning layers (i.e., convolution and fully-connected layer) should be a non-linear function."
    elif fault == "f010":
        return "The learnable parameters should be totally initialized once at the beginning of the training(missing init)"
    elif fault == "f011":
        return "A processing layer that operates on a N-dimensional tensors, should receive a valid input tensor with exactly N-dimensional shape(missing flatten )."
    elif fault == "f012":
        return "A last layer activation is required to transform the logits into probabilities for classification problem(bin missing sigmoid)."
    elif fault == "f013":
        return "A processing layer should receive sufficient-sized feature space to perform its spatial filtering or pooling."
    elif fault == "f014":
        return "mismatch shape : A reshape layer should never falsify the size of elements (i.e. first dimension)"
    elif fault == "f015":
        return "The loss should be correctly defined and connected to the layer in accordance with its input conditions (i.e.shape and type)-pre-activation"
    elif fault == "f016":
        return "The local window size for spatial filtering should generally increase or stay the same throughout the convolutional layers."
    elif fault == "f017":
        return "A last layer activation is required to transform the logits into probabilities for classification problem(bin wrong last layer activation)."
    elif fault == "f018":
        return "Dropout layer must be placed after the pooling layer to be more effective."
    elif fault == "f019":
        return "The area of feature maps and the width of fully-connected units should be progressively decreasing over the layers."
    elif fault == "f020":
        return "The loss should be correctly defined and connected to the layer in accordance with its input conditions (i.e.shape and type)-post_activation"
    elif fault == "f021":
        return "A reshape layer should preserve the total data elements/ A reshape layer should never falsify the size of elements (i.e. first dimension)."
    elif fault == "f022":
        return "The loss minimization problem should be solved iteratively with continuous update of parameters"
    elif fault == "f023":
        return "The number of feature maps should be gradually expanded while the feature map area is retracted."
    elif fault == "f024":
        return "The initialization of biases is preferred to be zeros."
    elif fault == "f025":
        return "Deep CNN should not apply pooling after every convolution."
    elif fault == "f026":
        return "Deep CNN should favor blocks of2,3or even 4 homogeneous convolutional layers with similar characteristics."
    elif fault == "f027":
        return "Max-pooling is the preferred down-sampling strategy(ineffective pooling)"
        
    else:
        return None


def main(inputGraphName="TF_lenet", parserType = "tf"):
    learnerNode = ""
    architectureNode = ""
    flags = {}
    edges = []
    faults = []
    layers = []
    nodeName = {}

    grooveOutputName = inputGraphName
    if parserType == "tf":
        graphFolderName = "TF_graphs"
    elif parserType == "keras":
        graphFolderName = "Keras_graphs"
    tree = ET.parse(f'{graphFolderName}/{grooveOutputName}.gst')
    root = tree.getroot()


    for edge in root.iter("{http://www.gupro.de/GXL/gxl-1.0.dtd}edge"):
        fromNode = edge.attrib.get("from")
        toNode = edge.attrib.get("to")
        flag = False
        if fromNode == toNode:
            for strTag in edge.iter("{http://www.gupro.de/GXL/gxl-1.0.dtd}string"):
                if strTag.text == "type:Learner":
                    learnerNode = fromNode
                elif strTag.text == "type:Architecture":
                    architectureNode = fromNode
                elif strTag.text == "type:Layer":
                    layers.append(fromNode)
                elif strTag.text.find("let:No = int:") != -1:
                    nodeName.update({fromNode: strTag.text.replace("let:No = int:", "")})
                elif strTag.text == "type:Faults":
                    faults.append(fromNode)
                elif strTag.text.find("flag:") != -1:
                    if fromNode in flags.keys():
                        temp = flags.get(fromNode)
                        temp.append(strTag.text.replace("flag:", ""))
                        flags.update({fromNode: temp})
                    else:
                        flags.update({fromNode: [strTag.text.replace("flag:", "")]})

        elif fromNode != toNode:
            for strTag in edge.iter("{http://www.gupro.de/GXL/gxl-1.0.dtd}string"):
                if strTag.text == "has-a" or strTag.text == "has":
                    directiveEdge = {"from": fromNode, "to": toNode}
                    edges.append(directiveEdge)


    # analyzing the result to relate faults and nodes
    buggyFlag = False
    output = ""

    # analyzing learner node
    learnerFaults = []
    architectureFault = []
    layerErrors = []
    layersFaults = {}
    for edge in edges:
        if edge.get("from") == learnerNode and edge.get("to") in faults and edge.get("to") in flags.keys():
            for item in flags.get(edge.get("to")):
                learnerFaults.append(item)
            edges.pop(edges.index(edge))
        if edge.get("from") == architectureNode and edge.get("to") in faults and edge.get("to") in flags.keys():
            for item in flags.get(edge.get("to")):
                architectureFault.append(item)
            edges.pop(edges.index(edge))


    if len(learnerFaults) != 0:
        buggyFlag = True
        output += "Learner ==> "

        for item in learnerFaults:
            output += faultCodeTranslator(item)
            if learnerFaults.index(item) != len(learnerFaults)-1:
                output += ", "

    if len(architectureFault) != 0:
        buggyFlag = True
        output += "Architecture ==> "
        for item in architectureFault:
            output += faultCodeTranslator(item)
            if architectureFault.index(item) != len(architectureFault) - 1:
                output += ", "

    preprocessing(learnerNode,flags, edges, faults)
    if buggyFlag and len(edges) != 0:
        output += "\n\r"

    if len(edges) != 0:
        buggyFlag = True

    buggyLayers = {}

    for item in edges:
        BuggyLayerName = item.get("from")
        buggyLayerNumber = nodeName.get(BuggyLayerName)
        layerErrors = flags.get(item.get("to"))
        report = "Layer {} ==> ".format(buggyLayerNumber)
        for item in layerErrors:
            report += faultCodeTranslator(item)
            if layerErrors.index(item) != len(layerErrors)-1:
                report += ", "

        buggyLayers.update({buggyLayerNumber:report})

    if len(buggyLayers) != 0:
        sortedBuggyLayers = dict(sorted(buggyLayers.items(), key=lambda s: int(s[0])))
        lastKey = list(sortedBuggyLayers.keys())[-1]
        for item in sortedBuggyLayers:
            output += sortedBuggyLayers.get(item)
            if item != lastKey:
                output += "\n\r"

    if not buggyFlag:
        output = "There is no identified fault in the DNN script"

    return output

if __name__ == "__main__":
    program_name = 'SO_deep_CNN_asymetry_blocksGrooveOut'
    result = main(program_name, "keras")
    print("result is :")
    print(result)
