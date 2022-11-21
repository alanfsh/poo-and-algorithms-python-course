import time
import sys

sys.setrecursionlimit(100000)

def factorial(n):
	respuesta = 1

	while n > 1:
		respuesta *= n
		n -= 1

	return factorial


def factorial_r(n):
	if n == 1:
		return 1
	
	return n * factorial_r(n-1)


if __name__ == '__main__':
	n = 5000

	inicio = time.time()
	factorial(n)
	fin = time.time()
	print(fin - inicio)

	inicio = time.time()
	factorial_r(n)
	fin = time.time()
	print(fin - inicio)