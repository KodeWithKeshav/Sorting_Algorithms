def mergeSort(arr):
    if len(arr)>1:
        third=max (1,(0+len(arr))//3)
        left = arr[:third]
        mid = arr[third:2*third]
        right = arr[2*third:]
        mergeSort(left)
        mergeSort(mid)
        mergeSort(right)
        i=j=k=l=0
        temp=[]
        while len(left)>i and len(mid)>j:
            if left[i]<mid[j]:
                temp.append(left[i])
                i+=1
            else:
                temp.append(mid[j])
                j+=1
        while len(left)>i:
            temp.append(left[i])
            i+=1
        while len(mid)>j:
            temp.append(mid[j])
            j+=1
        i=0
        while len(temp)>i and len(right)>k:
            if right[k]>temp[i]:
                arr[l]=temp[i]
                i+=1
            else:
                arr[l]=right[k]
                k+=1
            l+=1
        while len(temp)>i:
            arr[l]=temp[i]
            i+=1
            l+=1
        while len(right)>k:
            arr[l]=right[k]
            k+=1
            l+=1
arr=[3,5,2,4,6,9,7]
mergeSort(arr)
print(arr)