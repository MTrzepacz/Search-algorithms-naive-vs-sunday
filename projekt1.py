from random import choice

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

def prepareLastP(alfabet):
    dic = {i : -1 for i in alfabet}
    #print(dic)
    for i in "ABA":
        for key, value in dic.items():
            if (key == i):
                dic[i] = "ABA".rindex(i)
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
 

if __name__ == "__main__":
    dic = prepareLastP("ABCD")
    print(naiveV2("ACBCDABABBDB", "ABA"))
    print(sundayV2("ACBCDABABBDB","ABA",dic))