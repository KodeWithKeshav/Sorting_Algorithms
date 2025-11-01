def counting(arr):
    n=len(arr)
    countArr=[0]*(max(arr)+1)
    outputArr=[0]*n
    for i in range(n):
        countArr[arr[i]]+=1
    for i in range(1,(len(countArr))):
        countArr[i]+=countArr[i-1]
    for i in range(n-1,-1,-1):
        outputArr[countArr[arr[i]]-1]=arr[i]
        countArr[arr[i]]-=1
    return outputArr
arr=[2,4,1,6,4,2,3,1,6,5,4,2]
print(counting(arr))