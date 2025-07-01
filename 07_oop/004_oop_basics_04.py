# Creacion de atributos como en java (para ver la forma de python, ver el archivo 5)

from datetime import datetime
# Accesar a las variables protegidas utilizando metodos, no directamente

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email #protected variable
        self.password = password

    # para accesar una variable protegida:
    def get_email(self):
        print(f"Accessed at {datetime.now()}")
        return self._email
    

    # para modificar una variable protegida:
    def set_email(self, new_email):
        # Ejemplo de logica de validacion
        if "@" in new_email:
            self._email = new_email


user1 = User("Dan", "Dan@uol", "12345")


# Accesar la variable protegida
print(user1.get_email())

# Modificar una variable protegida
user1.set_email("dan@hotma")
print(user1.get_email())

print()
# Ejemplo con logica de validacion de email
user1.set_email("danhothot")
print(user1.get_email())