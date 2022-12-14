# Encontrar un elemento en una lista generada con random
import random

def busqueda_lineal(lista, objetivo):
	match = False

	for elemento in lista: # O(n) --> Complejidad algoritmica lineal
		if elemento == objetivo:
			match = True
			break

	return match


if __name__ == '__main__':
	tamano_de_lista = int(input('¿De que tamano será la lista?: '))
	objetivo = int(input('¿Qué número quieres encontrar?: '))

	lista = [random.randint(0,100) for i in range(0, tamano_de_lista)]

	encontrado = busqueda_lineal(lista, objetivo)

	print(lista)
	print(f'El elemento {objetivo} {"esta " if encontrado else "no esta "} en la lista')