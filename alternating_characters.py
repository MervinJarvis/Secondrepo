k=int(input())
j=0
for i in range(k):
    k=input()
    k=list(k)
    for i in range(0,len(k)-1):
        if k[i]==k[i+1]:
            print(k[i],k[i+1])
            #del(k[i+1])
            j+=1
        else:
            pass
    print(j)
    j=0
