t = int(input())
for x in range(1, t + 1):
    n = int(input())
    a =[]
    soma = 0
    for linhas in range(0,n):
        a.append(list(map(int, input().split())))
    for dimensao in range(0,n):
        soma+=a[dimensao][dimensao]
    countx=0
    breakx=0
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                if(a[i][j]==a[i][k] and j!=k):
                    countx=countx+1
                    breakx=1
                    break;
            if(breakx==1):
                breakx=0
                break;
    county=0
    breaky=0
    for j in range(0,n):
        for i in range(0,n):
            for k in range(0,n):
                if(a[i][j]==a[k][j] and i != k):
                    county=county+1
                    breaky=1
                    break;
            if(breaky==1):
                breaky=0
                break;
    print("Case #{}: {} {} {}".format(x,soma,countx,county))