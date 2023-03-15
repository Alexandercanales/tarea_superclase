class Jugador:
    tipo_jugador = "bueno"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def muestra_datos(self): 
        print("el muchacho se llama  " + self.nombre, "y tiene", self.edad , "años")

class defensa(Jugador):
    tipo_jugador = "malo"   

class central(Jugador):
    tipo_jugador = "regular" 

class delantero(Jugador):
    tipo_jugador = "mejor del mundo" 

jugador1 = Jugador("alexander" , 20)
jugador2 = Jugador("Goku" , 15)
jugador3 = Jugador("Vegeta" , 30)
jugador4 = Jugador("Broly" , 50)
 
jugador1.muestra_datos()
print("el jugador es ",Jugador.tipo_jugador)
jugador2.muestra_datos()
print("el jugador es ",defensa.tipo_jugador)
jugador3.muestra_datos()
print("el jugador es ",central.tipo_jugador)
jugador4.muestra_datos()
print("el jugador es ",delantero.tipo_jugador)


