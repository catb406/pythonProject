def merge_sort(arr, invcount):
    a=[]
    if len(arr)<2:
        return arr, invcount
    # elif len(arr)==2:
    #     if arr[0]<arr[1]:
    #         return arr, invcount
    #     else:
    #         arr[0], arr[1]=arr[1], arr[0]
    #         invcount+=1
    #         return arr, invcount
    left, invcount_l=merge_sort(arr[0:len(arr)//2], invcount)
    right, invcount_r=merge_sort(arr[len(arr)//2:len(arr)], invcount)
    invcount=invcount_r+invcount_l
    i=0
    j=0
    l=len(arr)
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            a.append(left[i])
            i += 1
        else:
            a.append(right[j])
            invcount += len(left) - i
            j += 1
    while i < len(left):
        a.append(left[i])
        i += 1

    while j < len(right):
        a.append(right[j])
        j += 1

    return a, invcount


invcount=0
n=input()
arr=list(map(int, input().split()))
print(merge_sort(arr, 0)[1])
