# Sirve para ordenar elementos en una lista, es de orden O(n²) --> NO EFICIENTE para listas grandes
import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n): # O(n²)
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiamos si el elemento a la derecha es mayor que el de la izquierda
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(lista)
    
    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('¿De que tamano será la lista?: '))

    # Generamos la lista
    lista = [random.randint(0,100) for i in range(0, tamano_de_lista)]
    print(lista)
    
    lista_ordenada = ordenamiento_burbuja(lista)
    
    print(lista_ordenada)