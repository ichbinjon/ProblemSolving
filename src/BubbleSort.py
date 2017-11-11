# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
def BubbleSort(a):
    num_swaps = 0
    for x in a:
        num_swaps = 0
        for index, n in enumerate(a):
            if (index + 1) > (len(a)-1):
                break
            if a[index] > a[index + 1]:
                temp = a[index]
                a[index] = a[index+1]
                a[index+1] = temp
                num_swaps += 1

        if num_swaps == 0:
            return (a, num_swaps)


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

list_swap = BubbleSort(a)
print("Array is sorted in %d swaps." % list_swap[1])
print("First Element: %d" % list_swap[0][0])
print("Last Element: %d" % list_swap[0][-1])
