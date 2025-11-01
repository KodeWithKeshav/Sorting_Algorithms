def selection_recursive(arr,n,index=0):
    if n == index:
        return -1
    k = min_index(arr,index,n-1)
    if k!=index:
        arr[k],arr[index]=arr[index],arr[k]
    selection_recursive(arr,n,index+1)
def min_index(arr,i,j):
    if i==j:
        return i
    k=min_index(arr,i+1,j)
    if arr[i]<arr[k]:
        return i
    else:
        return k
arr=[2,1,4,3,5,6]
selection_recursive(arr,len(arr))
print(arr)
