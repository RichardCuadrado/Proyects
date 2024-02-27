class Animal:
    nombre: str
    edad: str
    despierto: bool

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.despierto = False

    def consultar_estado(self):
        print(f"{self.nombre} está {'despierto' if self.despierto else 'dormido'}")

    def comer(self) -> None:
        if self.despierto:
            print(f"{self.nombre} está comiendo ", end= "")
        else:
            print(f"{self.nombre} está dormido ")
    
    def dormir(self) -> None:
        self.despierto = False
    
    def despertar(self) -> None:
        self.despierto = True

    def jugar(self) -> None:
        pass

class Perro(Animal):
    raza: str
    color_pelo: str

    def __init__(self, nombre: str, edad: int, raza: str, color: str) -> None:
        super().__init__(nombre, edad)
        self.raza = raza
        self.color_pelo = color
    
    def comer(self):
        super().comer()
        if self.despierto:
            print("croquetas")
    
    def jugar(self) -> None:
        if self.despierto:
            print(f"{self.nombre} está jugando con su pelota")
        else:
            print(f"{self.nombre} está dormido ")

class Gato(Animal):
    color_pelo: str

    def __init__(self, nombre: str, edad: int, color_pelo: str) -> None:
        super().__init__(nombre, edad)
        self.color_pelo = color_pelo

    def comer(self):
        super().comer()
        if self.despierto:
            print("concentrado")

    def jugar(self):
        if self.despierto:
            print(f"{self.nombre} está jugando con un laser")
        else:
            print(f"{self.nombre} está dormido ")

class Pez(Animal):
    especie: str
    color: str

    def __init__(self, nombre: str, edad: int, especie: str, color: str) -> None:
        super().__init__(nombre, edad)
        self.especie = especie
        self.color = color

    def comer(self) -> None:
        super().comer()
        if self.despierto:
            print("comida en hojuelas")
    
    def jugar(self) -> None:
        if self.despierto:
            print(f"{self.nombre} está jugando en una corriente de burbujas")
        else:
            print(f"{self.nombre} está dormido ")


if __name__ == "__main__":
    print("Hola, ingresa una opción para comenzar")
    print("Que animal deseas?: \n \t1. Perro \n \t2. Gato \n \t3. Pez \n")
    num = input()
    while True:
        if int(num) == 1:
            print("Ingresa el nombre de tu perro: ")
            nombre = input()
            print("Ingresa su edad: ")
            edad = input()
            print("Ingresa su raza:")
            raza = input()
            print("Ingresa su color: ")
            color = input()
            perro = Perro(nombre, int(edad), raza, color)
            while True:
                print("Que quieres hacer con tu mascota?: ")
                print("\t1. Consultar estado \n \t2. Despertar\n \t3. Dormir\n \t4. Comer \n \t5. Jugar")
                num = input()
                if int(num) == 1:
                    perro.consultar_estado()
                elif int(num) == 2:
                    perro.despertar()
                elif int(num) == 3:
                    perro.dormir()
                elif int(num) == 4:
                    perro.comer()
                elif int(num) == 5:
                    perro.jugar()
                elif int(num) == 0:
                    break
        elif int(num) == 2:
            print("Ingresa el nombre de tu gato: ")
            nombre = input()
            print("Ingresa su edad: ")
            edad = input()
            print("Ingresa su color: ")
            color = input()
            gato = Gato(nombre, int(edad), color)
            while True:
                print("Que quieres hacer con tu mascota?: ")
                print("\t1. Consultar estado \n \t2. Despertar\n \t3. Dormir\n \t4. Comer \n \t5. Jugar")
                num = input()
                if int(num) == 1:
                    gato.consultar_estado()
                elif int(num) == 2:
                    gato.despertar()
                elif int(num) == 3:
                    gato.dormir()
                elif int(num) == 4:
                    gato.comer()
                elif int(num) == 5:
                    gato.jugar()
                elif int(num) == 0:
                    break
        elif int(num) == 3:
            print("Ingresa el nombre de tu pez: ")
            nombre = input()
            print("Ingresa su edad: ")
            edad = input()
            print("Ingresa su especie:")
            especie = input()
            print("Ingresa su color: ")
            color = input()
            pez = Pez(nombre, int(edad), especie, color)
            while True:
                print("Que quieres hacer con tu mascota?: ")
                print("\t1. Consultar estado \n \t2. Despertar\n \t3. Dormir\n \t4. Comer \n \t5. Jugar")
                num = input()
                if int(num) == 1:
                    pez.consultar_estado()
                elif int(num) == 2:
                    pez.despertar()
                elif int(num) == 3:
                    pez.dormir()
                elif int(num) == 4:
                    pez.comer()
                elif int(num) == 5:
                    pez.jugar()
                elif int(num) == 0:
                    break
        elif int(num) == 0:
            break
        
