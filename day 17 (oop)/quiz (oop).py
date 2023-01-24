class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Max")
user_2 = User("002", "Jared")


user_1.follow(user_2)

print(user_2.followers)