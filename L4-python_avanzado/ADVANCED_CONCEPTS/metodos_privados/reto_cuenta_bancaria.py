"""
Implementar una clase
Cuenta Bancaria con un método protegido para actualizar 
el saldo y un método privado para registrar las transacciones internamente.

1. El método protegido (_actualizar_saldo) solo 
debe ser utilizado dentro de la clase y sus subclases.
2. El método privado (registrar_transaccion)
debe ser completamente interno y no accesible fuera de la clase.
"""


class CuentaBancaria():
    def __init__(self, user, ID, contraseña, balance):
        self.user = user
        self.id = ID
        self.password = contraseña
        self.balance = balance

    def _actualizar_saldo(self, monto):
        self.balance = monto
        self.__registrar_transaccion(f'Cambio de saldo: {monto}')
        print(f'Saldo actualizado. Nuevo balance: {self.balance}')
        
    def __registrar_transaccion(self, descripcion):
        print(f'registro interno: {descripcion}')

class CuentaAhorros(CuentaBancaria):
    def __init__(self, user, balance, interes):
        super().__init__(user, balance)
        self.interes = interes

    def aplicar_interes(self):
        monto_interes = self.balance * self.interes
        print(f'Aplicado interés de: ${monto_interes}')
        self._actualizar_saldo(monto_interes)
    


mi_ahorro = CuentaAhorros("Carlos", "12345", "admin123", 1000, 0.05)
print(f"--- Iniciando cuenta de {mi_ahorro.user} ---")
mi_ahorro.aplicar_interes() 
