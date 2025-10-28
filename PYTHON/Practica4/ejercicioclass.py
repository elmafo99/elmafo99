# Crea una clase llamada TarjetaTransporte que simule una tarjeta recargable para viajar en autobús o metro.
# Requisitos
# Atributos:
# usuario → nombre del dueño de la tarjeta.
# saldo → cantidad de dinero disponible (por defecto 0.0).
# Métodos:
# recargar(cantidad) →
# Si cantidad es menor o igual que 0, muestra un mensaje de error.
# Si es válida, aumenta el saldo y muestra un mensaje con el nuevo saldo.
# pagar_viaje(costo) →
# Si el saldo es suficiente, descuéntalo del saldo y muestra un mensaje con el nuevo saldo.
# Si no hay suficiente saldo, muestra un mensaje indicando que no se puede realizar el viaje.
# mostrar() → devuelve un texto con el nombre del usuario y el saldo actual.

class TarjetaTransporte:
    def __init__(self, usuario, saldo=0.0):
        self.usuario = usuario
        self.saldo = saldo
    
    def recargar(self, cantidad):
        if cantidad <= 0:
            print("Error")
        else:
            self.saldo += cantidad
            print(f"Se ha depositado un saldo de {cantidad} viajes. Nuevo saldo: {self.saldo}")
    
    def pagarViaje(self, coste):
        if self.saldo >= coste:
            self.saldo -= coste
            print(f"Viaje pagado. Nuevo saldo: {self.saldo} viajes")
        else:
            print("No se puede realizar el viaje. Saldo insuficiente")
    
    def mostrar(self):
        return(f"Titular: {self.usuario} , Saldo: {self.saldo}")

tarjeta1 = TarjetaTransporte("Elena", 0)
tarjeta1.recargar(20)
tarjeta1.pagarViaje(1)
print(tarjeta1.mostrar())





