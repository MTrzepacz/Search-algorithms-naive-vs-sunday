from random import choice

#This can be used to generate both pattern and 'searchString'
def randomString(dl: int, alfabet: str) -> str:
    result = ""
    for _ in range(dl):
        result += choice(alfabet)
    return result

def findPatternNaive(searchString, pattern):
  #In case of pattern of length 3 it's useless to start looking for it from last 2 indexes etc.
  compareCount = 0
  for startIndex in range(0, (len(searchString) - (len(pattern)-1))):
    matchedIndex = 0
    compareCount += 1
    while (matchedIndex < len(pattern) and searchString[startIndex + matchedIndex] == pattern[matchedIndex]):
      compareCount += 1
      matchedIndex += 1
      if (matchedIndex > 0 and matchedIndex == len(pattern)):
         print("found at index: " + str(startIndex)) 
  return compareCount  
 
def findPatternSunday(searchString, pattern, lastp):
  #In case of pattern of length 3 it's useless to start looking for it from last 2 indexes etc.
    startIndex = 0
    compareCount = 0
    for startIndex in range(0, (len(searchString) - (len(pattern)-1))):
        matchedIndex = 0
        compareCount += 1
        if(startIndex >= len(searchString)): return compareCount
        while (matchedIndex < len(pattern) and searchString[startIndex + matchedIndex] == pattern[matchedIndex]):
          compareCount += 1
          matchedIndex += 1
          if (matchedIndex > 0 and matchedIndex == len(pattern)):
             print("found at index: " + str(startIndex))
          startIndex += startIndex + len(pattern)
          if(startIndex < len(searchString)):
              startIndex = startIndex - lastp[searchString[startIndex]]     
    return compareCount   


def matchesAt(searchString, pattern, position):
    for i in range(0, len(pattern)):
        if(pattern[i] != searchString[position+i]):
           return False
    else:    
        return True

def naiveV2(searchString, pattern):
    for i in range(0, len(searchString) - len(pattern)):
        if(matchesAt(searchString, pattern, i)):
            print("matches at: " + str(i))


if __name__ == "__main__":
    print(findPatternNaive("ACBCDABA", "ABA"))
    dic = {i : -1 for i in "ABCD"}
    #print(dic)
    for i in "ABA":
        for key, value in dic.items():
            if (key == i):
                dic[i] = "ABA".rindex(i)
    #print(dic)
   # print(findPatternSunday("ACBCDABABBDB", "ABA", dic))
    print(naiveV2("ACBCDABABBDB", "ABA"))
    #print(matchesAt("ACBCDABABBDB", "ABA", 7))