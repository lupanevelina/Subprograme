def creare_lista():
    n=int(input("Nr de elemente: "))
    lista_locala=[]
    for i in range(n):
        elem=input("Elementul "+ str(i) +" este:")
        Float = float(elem) 
        if type(elem)==float:
            lista_locala.append(str(elem))
    return lista_locala
lista1=creare_lista()
print(lista1)