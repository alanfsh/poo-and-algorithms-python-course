def morral(tamano_morral, pesos, valores, n):
    if n == 0 or tamano_morral == 0:
        return 0
    
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)
    
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
               morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [20, 30, 50]
    pesos = [10, 30, 50]
    tamano_morral = 33
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)