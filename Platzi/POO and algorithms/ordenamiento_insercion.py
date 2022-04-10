import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]  #56
        posicion_actual = indice     #1
                                                  #92 > 56  
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista   
        

if __name__== "__main__":
    tamano_de_lista = int(input("De que tamaño sera la lista "))
    #objetivo = int(input("Que número quieres encontrar"))
    
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)
    
    
    print(lista_ordenada)