def findSubstring(s, k):
    f=abs(len(s)-k)
    h=['a','e','i','o','u']
    p=[]
    g=0
    l={}
    print(''.join(h))
    for i in range(f+1):
        for j in range(i,k+i):
            p.append(s[j])
        for d in p:
            if d in h:
                g+=1
        p=str(p)
        l.update({p:g})
        p=list(p)
        p.clear()
        g=0
    key=max(l,key=l.get)
    #print(key)
    key=str(key)
    key=list(key)
    print(type(key))
    print(''.join(key))
    #key=key.replace("'",'')
    #key=key.replace(",",'')
    #key=key.replace("[",'')
    #key=key.replace("]",'')
    #key=key.replace(" ",'')
    return key
s = input()
k = int(input().strip())
findSubstring(s, k)
