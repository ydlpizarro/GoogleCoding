t = int(input())
def remover(cadeia):
        cadeia=cadeia.split(')(')
        retorno = ''
        for x in range(0,len(cadeia)):
            retorno = retorno+cadeia[x]
        return retorno
def compare(string1,string2):
    return(string1==string2)
for x in range(1,t+1):
    a=[]
    a=input()
    arrays = []
    arrays.append([int(a[0])])
    for i in range(1,len(a)):
        if(int(a[i-1]) == int(a[i])):
            arrays[len(arrays)-1].append(int(a[i]))
        else:
            arrays.append([int(a[i])])        
    saida=''
    for i in range(0,len(arrays)):
        textol=''
        textor=''
        texto =''
        textol = '('*arrays[i][0]
        textor = ')'*arrays[i][0]
        for k in range(0,len(arrays[i])):
            texto = texto+str(arrays[i][k])
        texto = textol+texto+textor
        saida = saida+texto
    while(saida!=remover(saida)):
        saida=remover(saida)
    print("Case #{}: {}".format(x,saida))