class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email


user1 = User("Don", "don@email", "123456")
user1.email = "this is not an email"
print(user1.email)