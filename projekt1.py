import matplotlib.pyplot as plt
import numpy as np
from random import choice
from matplotlib.collections import EventCollection

#This can be used to generate both pattern and 'searchString'
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

def prepareLastP(alfabet, pattern):
    dic = {i : -1 for i in alfabet}
    for i in pattern:
        for key, value in dic.items():
            if (key == i):
                dic[i] = pattern.rindex(i)
    return dic            


def naiveV2(searchString, pattern):
    compareCount = 0
    #+1 because of python in range
    for i in range(0, len(searchString) - len(pattern) + 1):
        res = matchesAt(searchString, pattern, i)
        compareCount += res[1]
        if(res[0]):
            print("matches at: " + str(i))
    return compareCount

def sundayV2(searchString, pattern, lastp):
    compareCount = 0
    #start index
    i = 0
    while ( i <= len(searchString) - len(pattern)):
        res = matchesAt(searchString, pattern, i)
        compareCount += res[1]
        if(res[0]):
            print("matches at: " + str(i))    
        i = i + len(pattern)
        if(i < len(searchString)):
            i = i - lastp[searchString[i]]
    return compareCount        
 

def createResultGrapth(xAxisParameters, yAxisParametersNaive,yAxisParametersSunday,patternLength):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(xAxisParameters,yAxisParametersNaive, label = "naive" )
    ax.plot(xAxisParameters,yAxisParametersSunday, label = "sunday" )
    ax.set_xlabel('Length of searchString')
    ax.set_ylabel('Compare Count')
    ax.set_title("Search algorithm - Naive vs Sunday with patten length = " + str(patternLength))
    ax.legend()
    fig.show()    


if __name__ == "__main__":
    dic = prepareLastP("ABCD", "ABA")
    print(naiveV2("ACBCDABABBDB", "ABA"))
    r1 = naiveV2("ACBCDABABBDB", "ABA")
    r2 = naiveV2("ACBCDABABBDBACBCDABABBDB", "ABA")
    r3 = naiveV2("ACBCDABABBDBACBCDABABBDBACBCDABABBDB", "ABA")
    print(sundayV2("ACBCDABABBDB","ABA",dic))
    s1 = sundayV2("ACBCDABABBDB","ABA",dic)
    s2 = sundayV2("ACBCDABABBDBACBCDABABBDB","ABA",dic)
    s3 = sundayV2("ACBCDABABBDBACBCDABABBDBACBCDABABBDB","ABA",dic)
    
   
    createResultGrapth([12,24,36], [r1, r2, r3],[s1, s2, s3], 3 )
   # fig, ax = plt.subplots()  # Create a figure containing a single axes.
   # ax.plot([12,24,36],[r1, r2, r3], label = "naive" )
   # ax.plot([12,24,36],[s1, s2, s3], label = "sunday" )
   # ax.set_xlabel('Length of searchString')
   # ax.set_ylabel('Compare Count')
   # ax.set_title("Search algorithm - Naive vs Sunday with patten length = 3")
   # ax.legend()
   # fig.show()
    