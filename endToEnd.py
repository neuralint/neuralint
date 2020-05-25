import parser_TF
import parser_Keras
import os
import grooveParser
import sys
import ast

def parserType(fileName):
    try:
        source = open(f"{fileName}.py", "r")
    except:
        raise SystemExit("The file doesn't exist or it isn't a Python script ...")
    
    tree = ast.parse(source.read())
    tree_body = tree.body
    for item in tree_body:
        if isinstance(item, ast.Import):
            if item.names[0].name == "keras":
                return "keras"
            elif item.names[0].name == "tensorflow":
                return "tf"
        if isinstance(item, ast.ImportFrom):
            if "keras" in item.module:
                return "keras"
            elif "tensorflow" in item.module:
                return "tf"

def parsDnnScript(fileName, parser = "tf" , inputSize=[128, 20], outputSize=[128, 10], groovePath = "groove-5_7_4-bin/groove-5_7_4/bin/", grammarName="DNN-metamodel"):
    FileNameWithoutPath = fileName.split(os.path.sep)[-1]
    grooveOutputFileName = f"{FileNameWithoutPath}GrooveOut"
    parser_type = parser

    if parser_type == "keras":
        parser = "keras"

        try:
            print("Generating model (graph)  ... \n")
            parser_Keras.main(fileName, input_size=inputSize, output_size=outputSize)
            print("Running Model Checker (Groove) ... \n")
            os.system(
                f'java -jar {groovePath}Generator.jar -f Keras_graphs/{grooveOutputFileName}.gst -s bfs {grammarName}.gps Keras_graphs/{FileNameWithoutPath}.gst')
        except:
            return f"{FileNameWithoutPath}.py\n\rError: input file is not valid or not match with selected parser type"


    elif parser_type == "tf":
        parser = "tf"

        try:
            print("Generating model (graph)  ... \n")
            parser_TF.main(fileName, input_size= inputSize, output_size=outputSize)
            print("Running Model Checker (Groove) ... \n")
            os.system(
                f'java -jar {groovePath}Generator.jar -f TF_graphs/{grooveOutputFileName}.gst -s bfs {grammarName}.gps TF_graphs/{FileNameWithoutPath}.gst')
        except:
            return f"{FileNameWithoutPath}.py\n\rError: input file is not valid or not match with selected parser type"


    try:
        result = f"{FileNameWithoutPath}.py\n\r" + grooveParser.main(grooveOutputFileName, parserType = parser)
        return result
    except:
        return f"{FileNameWithoutPath}.py\n\rError: input file is not valid or not match with selected parser type"

def checkInOutSize(inOut):

    if inOut[0] != '[' or inOut[len(inOut)-1] != ']':
        return False
    inOut = inOut[1:len(inOut)-1]
    inOutList = inOut.split(",")
    inOutList = list(map(int, inOutList))

    return inOutList

def main():
    arguments = sys.argv
    if len(arguments) != 6:
        raise SystemExit('usage: endtoend.py [input filename] [input size] [output size] [parser type] [output filename]')
    else:
        file_folderName = arguments[1]
        inputSize = checkInOutSize(arguments[2])
        outputSize = checkInOutSize(arguments[3])

        if inputSize == False or outputSize==False:
            raise SystemExit("Error : Input and output size should be entered as array([x1, x2, x3, ...]).")

        parserName = arguments[4].lower()
        resultFileName = arguments[5]
        if parserName != "tf" and parserName != "keras":
            raise SystemExit("Error : Parser type should be 'tf' or 'keras'")
    try:
        outputFile = open(f"{resultFileName}.txt" ,"w", encoding="ISO-8859-1")
    except IOError:
        raise SystemExit("Error : output filename should meet host operating system filename rules")

    extention = os.path.splitext(file_folderName)[1]

    if extention == ".py":
        output = parsDnnScript(fileName = os.path.splitext(file_folderName)[0], inputSize = inputSize ,outputSize = outputSize , parser=parserName)
        outputFile.write(output)
    else:
        raise SystemExit("Error : input should be a python script file")
if __name__ == '__main__':
    main()

