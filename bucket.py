def bucket(arr):
    n=len(arr)
    buckets=[]
    for i in range(n):
        buckets.append([])
    for i in range(n):
        ins=int((arr[i]/max(arr))*(n-1))
        buckets[ins].append(arr[i])
    for bucket in buckets:
        insertionSort(bucket)
    index=0
    for bucket in buckets:
        for num in bucket:
            arr[index]=num
            index+=1
def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=[1.2,3.4,2.2,4.9,0.74,9.88,8.63]
bucket(arr)
print(arr)