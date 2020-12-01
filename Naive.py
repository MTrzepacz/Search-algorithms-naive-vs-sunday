from CommonFunctions import matchesAt as matchesAt

def naive(searchString, pattern):
    compareCount = 0
    #+1 because of python in range
    for i in range(0, len(searchString) - len(pattern) + 1):
        res = matchesAt(searchString, pattern, i)
        compareCount += res[1]
        if(res[0]):
            print("matches at: " + str(i))
    return compareCount