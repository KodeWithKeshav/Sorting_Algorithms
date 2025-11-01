def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
arr=[1,2,4,3,7,6,10,9]
selection_sort(arr)
print(arr)