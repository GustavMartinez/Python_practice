class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi! {user.username}, it is {self.username}")



user1 = User("Ricardo", "figa@123", "123")
user2 = User("Alberto", "alt@123", "456")

user1.say_hi_to_user(user1)