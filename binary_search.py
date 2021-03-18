A = list(map(int, input().split()))
res = []
j = -1
left = 0
right = len(A) - 1
while left <= right:
    i = (right + left)//2
    if i == A[i]:
        j = i
        break
    elif i > A[i]:
        left = i + 1
    elif i < A[i]:
        right = i - 1

print(j)
