class BaseClass:
    def __init__(self):
        self._protected_variable = 'protected'
        self.__provate_variable = 'Privated'

    def _protected_method(self):
        print('Este es un método protegido')

    def __private_method(self):
        print('Esto es un método privado')

    def public_method(self):
        self.__private_method()


base = BaseClass()
#print(base._protected_variable)
# base._protected_method()

#base.public_method()
print(base.__provate_variable)