arr=[1,2,3,4,5]
l=[]
a=0
k=tuple(arr)
for i in range(len(arr)):
    arr=list(k)
    del(arr[i])
    a+=sum(arr)
    l.append(a)
    print(l)
    a=0
print(min(l),max(l))
#miniMaxSum(arr)
