def percorre_lista(lista): 
    tam = len(lista)
    # len vai pegar o tamanho da lista
    for i in range(tam):
        # range irá criar uma lista com o tamanho dado(indo de 0 ao tam)
        for j in range(0, tam-i-1):
            if lista[j] > lista[j+1] : 
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # print(lista[j])
                # print(lista[j + 1])
                # print(lista)
    print(lista)

a = [4,6,2,1,7,8,3,0,5,9]

teste = percorre_lista(a)



