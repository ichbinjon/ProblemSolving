#https://www.hackerrank.com/challenges/ctci-making-anagrams
#There are way way way more elegant solutions on HackerRank.
#I could have done this with just one array and taken absolute values.
#Took way longer than it should have as well.
def number_needed(a, b):
    freqA = frequencyDictionary(a)
    freqB = frequencyDictionary(b)

    updatedDict = updateDictionary(freqA,freqB)
    anagramChars = sum(updatedDict.values())*2
    allChars = sum(freqA.values()) + sum(freqB.values())
    #print(allChars)
    numberToRemove= allChars - anagramChars

    return numberToRemove


def frequencyDictionary(a):
	ndict = {}
	for x in a:
		if(x in ndict):
			ndict[x] = ndict.get(x) + 1
		else:
			ndict[x] = 1
	return ndict

def updateDictionary(dictA,dictB):
	commonDict={}
	if(len(dictA) > len(dictB)):
		for x in dictB:
			if (x in dictA and x in dictB):
				commonDict[x] = min(dictA.get(x),dictB.get(x))
			else:
				pass
	else:
		for x in dictA:
			if (x in dictA and x in dictB):
				commonDict[x] = min(dictA.get(x),dictB.get(x))
			else:
				pass

	return commonDict




a = input().strip()
b = input().strip()

print(number_needed(a, b))
