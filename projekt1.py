import matplotlib.pyplot as plt
from random import choice
from string import ascii_uppercase

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
 

def createResultGrapth(xAxisParameters, yAxisParametersNaive,yAxisParametersSunday,alphabetLength, patternLength):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(xAxisParameters,yAxisParametersNaive, label = "naive" )
    ax.plot(xAxisParameters,yAxisParametersSunday, label = "sunday" )
    ax.set_xlabel('Length of searchString')
    ax.set_ylabel('Compare Count')
    ax.set_title("Search algorithm - Naive vs Sunday with patten length = " + str(patternLength) + " and alphabet length = " + str(alphabetLength))
    ax.legend()
    fig.show()    


if __name__ == "__main__":
    
    for alpLength in range(3,10,3):
        for patternLength in range (3, 10, 3):
    #Creating alphabet, pattern to search and searchString length table
            print("Proccesing for alpLength: " + str(alpLength) + "and patternLength: " + str() )
            searchStringLength = [50, 150, 500]
            alphabet = ascii_uppercase[:alpLength]
            pattern = randomString(3, alphabet)
    
            print(pattern)
    
    #Running Naive algorithm
            r1 = naiveV2(randomString(searchStringLength[0], alphabet), pattern)
            r2 = naiveV2(randomString(searchStringLength[1], alphabet), pattern)
            r3 = naiveV2(randomString(searchStringLength[2], alphabet), pattern)
  
    #Running Sunday algorithm with 
            dic = prepareLastP(alphabet, pattern)
            s1 = sundayV2(randomString(searchStringLength[0], alphabet),pattern,dic)
            s2 = sundayV2(randomString(searchStringLength[1], alphabet),pattern,dic)
            s3 = sundayV2(randomString(searchStringLength[2], alphabet),pattern,dic)
    
            print("Naive counts:")
            print(*[str(r1),str(r2),str(r3)], sep = ' ')
    
            print("Sunday counts:")
            print(*[str(s1),str(s2),str(s3)], sep = ' ')
    #Creating result Graph
            createResultGrapth([50,150,500], [r1, r2, r3],[s1, s2, s3], len(alphabet), len(pattern))
    