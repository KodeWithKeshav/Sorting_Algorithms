def merge_sort(arr):
    if len(arr)>1:
        mid = (0+len(arr))//2
        left = arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while len(left)>i and len(right)>j:
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]= right[j]
                j+=1
            k+=1
        while len(left)>i:
            arr[k]=left[i]
            i+=1
            k+=1
        while len(right)>j:
            arr[k]=right[j]
            j+=1
            k+=1
arr=[2,1,4,3,6,5,9,10]
merge_sort(arr)
print(arr)