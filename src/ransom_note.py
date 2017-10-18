#https://www.hackerrank.com/challenges/ctci-ransom-note

def ransom_note(magazine, ransom):
	magazine_dict = {}
	ransom_dict = {}

	for x in magazine:
		if x in magazine_dict:
			magazine_dict[x] +=1
		else:
			magazine_dict[x]=1

	for x in ransom:
		if x in ransom_dict:
			ransom_dict[x] += 1
		else:
			ransom_dict[x]=1

	for x in ransom_dict:
		if x in magazine_dict:
			if magazine_dict[x] >= ransom_dict[x]:
				pass
			else:
				return False
		else:
			return False
	return True

    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")