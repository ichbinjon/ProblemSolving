# https://www.hackerrank.com/challenges/ctci-array-left-rotation


def array_left_rotation(a, n, k):
    # Space O(1) Computation O(n) -> actually O(n*k)
    for x in range(0, k, 1):
        temp = a.pop(0)
        a.append(temp)
    return a


def array_left_rotation_2(a, n, k):
    # another solution using list slicing
        return a[k:]+a[:k]


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
