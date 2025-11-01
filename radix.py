def counting_radix(arr,exp1):
    n=len(arr)
    output=[0]*n
    count=[0]*10
    for i in range(n):
        index=arr[i]//exp1
        count[index%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        index=arr[i]//exp1
        output[count[index%10]-1]=arr[i]
        count[index%10]-=1
    for j in range(n):
        arr[j]=output[j]
def radix(arr):
    maxele=max(arr)
    exp1=1
    while maxele//exp1>=1:
        counting_radix(arr,exp1)
        exp1*=10
arr=[12,122,23,45,456,123,169,1028]
radix(arr)
print(arr)