def creare_lista():
    n=int(input("Nr de elemente: "))
    lista_locala=[]
    for i in range(n):
        elem=input("Elementul "+ str(i) +" este:")
        if(ord(elem) >= 48 and ord(elem) <= 57):
            lista_locala.append(elem)
        while(ord(elem) <= 48 and ord(elem) >= 57):
            elem=input("Introduceti elementul "+ str(i) +" inca o data:")
            lista_locala.extend(elem)

    return lista_locala
lista1=creare_lista()
print(lista1)