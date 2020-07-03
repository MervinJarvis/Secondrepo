n,m=map(int,input().split())
k=[]
j=[]
a,b=0,1
for i in range(n):
    l=list(map(int,input().split()))
    k.append(l)
    #print(l)
for i in range(n-1):
    print(k[i][1] + k[i+1][1])
    if k[i][1] + k[i+1][1] == m:
        a+=k[i][0] + k[i+1][0] 
        j.append(a)
        a=0
        b=0
if b==0:
    print(max(j))
else:
        print("Got caught!")
