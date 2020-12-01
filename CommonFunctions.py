from random import choice
import matplotlib.pyplot as plt

def randomString(dl: int, alfabet: str) -> str:
    result = ""
    for _ in range(dl):
        result += choice(alfabet)
    return result

def matchesAt(searchString, pattern, position):
    compareCount = 0
    for i in range(0, len(pattern)):
        compareCount += 1
        if(pattern[i] != searchString[position+i]):
           return [False, compareCount]
    else:    
        return [True, compareCount]
    
def createResultGrapth(xAxisParameters, yAxisParametersNaive,yAxisParametersSunday,alphabetLength, patternLength):
    fig, ax = plt.subplots()
    ax.plot(xAxisParameters,yAxisParametersNaive, label = "naive" )
    ax.plot(xAxisParameters,yAxisParametersSunday, label = "sunday" )
    ax.set_xlabel('Length of searchString')
    ax.set_ylabel('Compare Count')
    ax.set_title("Search algorithm - Naive vs Sunday with pattern length = " + str(patternLength) + " and alphabet length = " + str(alphabetLength))
    ax.legend()
    fig.show()        