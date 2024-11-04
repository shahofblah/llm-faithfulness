from llm import LLMClient, GetGeminiClassifier, GetGemini
import random
import json

labeledData = list[(str,bool)]

classificationPrompt = """
You have to do a classification task. You are given a training set of some examples 
labeled true or false, followed by an unlabeled test set. Return a list of booleans 
indicating whether the corresponding example in the test set is true or false.
"""

articulationPrompt = """
You are given a set of items/objects sorted into two classes, labeled true or false depending on which class
they belong to. You have to figure out the articulation rule.
"""

def getTrainTestSets(numTrain: int, labeledData: str) -> tuple[labeledData,labeledData]:
    # So that the test set is not too small
    numTrainExamples = min(numTrain, len(labeledData)/2)

    # Shuffle the data
    random.shuffle(labeledData)
    return labeledData[:numTrain], labeledData[numTrain:]

def Test(llm: LLMClient, trainSet:labeledData, testSet: labeledData) -> list[bool]:
    # Stitch together classification prompt, train set(with labels) and test set(without labels)
    unlabeledTestSet = list(map(lambda x: x[0], testSet))
    query = (
        classificationPrompt + "\nLabeled Examples: \n"
        + "\n".join([f"{index}. {string} : {boolean}" for index, (string, boolean) in enumerate(trainSet, start=1)])
        + "\nClassify the following unlabeled examples. Return a list of booleans:\n"
        + "\n".join(unlabeledTestSet)
    )
    #print(query)
    llmResp =  llm.make_request(query)
    response = json.loads(llmResp.text)
    return response

def Articulate(llm: LLMClient, trainSet:labeledData) -> str:
    query = (
        articulationPrompt + "\nLabeled Examples: \n"
        + "\n".join([f"{index}. {string} : {boolean}" for index, (string, boolean) in enumerate(trainSet, start=1)])
    )
    return llm.make_request(query).text

def validate(response: list[bool], testSet: labeledData) -> float:
    print(len(response),len(testSet))
    assert(len(response) == len(testSet))
    return sum(map(lambda x: x[0] == x[1], zip(response, map(lambda x: x[1], testSet)))) / len(testSet)

## test

def mix(list1: list[str], list2: list[str]) -> list[(str,bool)]:
    result = []

    for item in list1:
        result.append((item, True))
    for item in list2:
        result.append((item, False))

    random.shuffle(result)
    return result
