# Encontrar un elemento en una lista generada mediante busqueda binaria
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
	# Si inicio de busqueda es mayor que el final ya nos pasamos
	if comienzo > final:
		return False

	medio = (comienzo + final) // 2
	if lista[medio] == objetivo:
		return True
	elif lista[medio] > objetivo:
		return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
	else:
		return busqueda_binaria(lista, medio + 1, final, objetivo)


if __name__ == '__main__':
	tamano_de_lista = int(input('¿De que tamano será la lista?: '))
	objetivo = int(input('¿Qué número quieres encontrar?: '))

	# Ordenamos la lista
	lista = sorted([random.randint(0,100) for i in range(0, tamano_de_lista)])

	encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

	print(lista)
	print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')