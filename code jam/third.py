t = int(input())
def getKey(item):
    return item[0]
def disponible(vetor,c,j,pos):
    if(len(c)!=0):
        if(vetor[c[len(c)-1]][1]<=vetor[pos][0]):
            return 'C'
        elif(vetor[j[len(j)-1]][1]<=vetor[pos][0]):   
            return 'J'
    if(len(j)!=0):        
        if(vetor[j[len(j)-1]][1]<=vetor[pos][0]):   
            return 'J' 
        elif(vetor[c[len(c)-1]][1]<=vetor[pos][0]):
            return 'C'
    return 'Error'
        
for x in range(1,t+1):
    n = int(input())
    arrays=[]
    saida=[]
    mensagemv=[]
    c=[]
    j=[]
    mensagem = ''
    for i in range(1,n+1):
        a=list(map(int,input().split()))
        arrays.append(a)
    saida=sorted(arrays,key=getKey)
    for k in range(0,n-1):
        if(saida[k][1]<=saida[k+1][0]):
            if(len(c)==0 and len(j)==0):
                c.append(k)
                j.append(k+1)
                continue;
            if(disponible(saida,c,j,k+1)=='C'):
                c.append(k+1)
                continue;
            if(disponible(saida,c,j,k+1)=='J'):
                j.append(k+1)
                continue;
            if(disponible(saida,c,j,k+1)=='Error'):
                mensagem = "IMPOSSIBLE"
                break;
        else:
            if(len(c)==0 and len(j)==0):
                c.append(k)
                j.append(k+1)
                continue;
            if(disponible(saida,c,j,k+1)=='C'):
                c.append(k+1)
                continue;
            if(disponible(saida,c,j,k+1)=='J'):
                j.append(k+1)
                continue;
            if(disponible(saida,c,j,k+1)=='Error'):
                mensagem = "IMPOSSIBLE"
                break;
    c=list(dict.fromkeys(c))
    j=list(dict.fromkeys(j))
  
    if(mensagem=="IMPOSSIBLE"):
        print("Case #{}: {}".format(x,mensagem))        
    else:
        for w in range(0,n):
            for q in range(0,n):
                if(arrays[w][0]==saida[q][0]) and (arrays[w][1]==saida[q][1]):
                    if(q in c):
                        mensagem=mensagem+'C'
                    if(q in j):
                        mensagem=mensagem+'J'
        print("Case #{}: {}".format(x,mensagem))