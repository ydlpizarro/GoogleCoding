def getKey(item):
    return item[0]
t = int(input())
for x in range(1,t+1):
    n=0
    b=0
    a=[]
    c=[]
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))
    c=sorted(c)
    soma=0
    count = 0
    for j in range(0,a[0]):
        if(c[j]+soma<=a[1]):
            soma=soma+c[j]
            count=count+1
        else:
            break
    print("Case #{}: {}".format(x,count))