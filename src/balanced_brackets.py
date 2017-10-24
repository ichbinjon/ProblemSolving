#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    stack = []
    closedBrackets = [')',']','}']
    for char in expression:
	    if(char in closedBrackets):
	    	if stack == []:
	    		return False
	    	if (char == ')' and stack[-1] == '('):
	    		stack.pop()
	    		continue
	    	elif (char == '}' and stack[-1] == '{'):
	    		stack.pop()
	    		continue
	    	elif (char == ']' and stack[-1] == '['):
	    		stack.pop()
	    		continue
	    	else:
	    		return False
	    else:
	    	stack.append(char)

    if len(stack) == 0:
        return True
    else:
        return False


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
       	print("YES")
    else:
        print("NO")
