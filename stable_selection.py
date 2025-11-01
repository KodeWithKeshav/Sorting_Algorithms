def stable_selection(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        key = arr[min]
        while min>i:
            arr[min]=arr[min-1]
            min-=1
        arr[i]=key
arr=[2,1,3,4,2,5,6]
stable_selection(arr)
print(arr)