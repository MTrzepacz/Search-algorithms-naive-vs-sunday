from CommonFunctions import matchesAt as matchesAt

def prepareLastP(alfabet, pattern):
    dic = {i : -1 for i in alfabet}
    for i in pattern:
        for key, value in dic.items():
            if (key == i):
                dic[i] = pattern.rindex(i)
    return dic            

def sunday(searchString, pattern, lastp):
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