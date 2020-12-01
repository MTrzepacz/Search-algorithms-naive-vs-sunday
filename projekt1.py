from string import ascii_uppercase

from CommonFunctions import randomString as randomString
from CommonFunctions import matchesAt as matchesAt
from CommonFunctions import createResultGrapth as createResultGrapth

from Naive import naive as naive

from Sunday import sunday as sunday
from Sunday import prepareLastP as prepareLastP

if __name__ == "__main__":
    for alpLength in range(3,10,3):
        for patternLength in range (3, 10, 3):
    #Creating alphabet, pattern to search and searchString length table
            print("Proccesing for alpLength: " + str(alpLength) + " and patternLength: " + str(patternLength))
            searchStringLength = [50, 150, 500]
            alphabet = ascii_uppercase[:alpLength]
            pattern = randomString(patternLength, alphabet)
    
            print(pattern)
    
    #Running Naive algorithm
            r1 = naive(randomString(searchStringLength[0], alphabet), pattern)
            r2 = naive(randomString(searchStringLength[1], alphabet), pattern)
            r3 = naive(randomString(searchStringLength[2], alphabet), pattern)
  
    #Running Sunday algorithm with 
            dic = prepareLastP(alphabet, pattern)
            s1 = sunday(randomString(searchStringLength[0], alphabet),pattern,dic)
            s2 = sunday(randomString(searchStringLength[1], alphabet),pattern,dic)
            s3 = sunday(randomString(searchStringLength[2], alphabet),pattern,dic)
    
            print("Naive counts:")
            print(*[str(r1),str(r2),str(r3)], sep = ' ')
    
            print("Sunday counts:")
            print(*[str(s1),str(s2),str(s3)], sep = ' ')
    #Creating result Graph
            createResultGrapth([50,150,500], [r1, r2, r3],[s1, s2, s3], len(alphabet), len(pattern))
    