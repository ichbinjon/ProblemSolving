#https://www.hackerrank.com/challenges/ctci-array-left-rotation
# Space O(1) Computation O(n)
def array_left_rotation(a, n, k):
      for x in range(0,k,1):
        temp = a.pop(0)
        a.append(temp)  
      return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
