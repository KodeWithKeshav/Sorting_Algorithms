def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heapSort(arr):
    n=len(arr)
    temp=[]
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,-1,-1):
        arr[i],arr[0]=arr[0],arr[i]
        x=arr.pop()
        temp.append(x)
        heapify(arr,i,0)
    arr.extend(temp[::-1])
arr=[3,2,1,6,5,7,4]
heapSort(arr)
print(arr)
