class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} esta caminando')
    

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'{self.nombre} esta moviendose en bicicleta')


def main():
    persona = Persona('Pedro')
    persona.avanza()

    ciclista = Ciclista('Juan')
    ciclista.avanza()


if __name__ == '__main__':
    main()