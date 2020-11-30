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
      #return True
         print("found at index: " + str(startIndex)) 
  #return False
  return compareCount  
#print(randomString(10, "ABC"))
         

if __name__ == "__main__":
    searchString = randomString(10,"ABC")
    print(searchString)
    pattern = randomString(2,"ABC")
    print(pattern)
    print(findPatternNaive("AAAABAAA", "BAB"))
    #print(findPatternNaive(searchString,pattern))