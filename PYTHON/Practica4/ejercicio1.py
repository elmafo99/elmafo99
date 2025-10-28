# Ejercicio 1. UTILIZAR CLASS

# Crea una clase CuentaBancaria con:

# Atributos: titular (str) y saldo (float).

# Método depositar(cantidad) que sume al saldo (no permite montos ≤ 0).

# Método mostrar() que devuelva un string del estilo: "Titular: Ana | Saldo: 125.50€".

class CuentaBancaria:
    def __init__(self, titular, saldo =0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor o igual a 0")
        else:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad:2f}€. Nuevo saldo: {self.saldo:2f}€")
    
    def mostrar(self):
        return f"Titular: {self.titular}" , f"Saldo: {self.saldo}"

cuenta1 = CuentaBancaria("Elena", 500.0)
cuenta1.depositar(500.0)
cuenta1.depositar(-50.0)
print(cuenta1.mostrar())