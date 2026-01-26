class User:
    def __init__(self, user_id, user_name, user_age):
        self.id = user_id
        self.user_name = user_name
        self.age = user_age
        self.followers = 0

    def new_follower(self):
        self.followers +=1


user_1 = User("012", "Gustavo", 19)

print(user_1.id)
print(user_1.user_name)
print(user_1.age)
print(user_1.followers)

user_1.new_follower()
user_1.new_follower()
user_1.new_follower()
print(f"Total de followers: {user_1.followers}")
