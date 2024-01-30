class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1



user_1 = User("001", "Kev")
user_2 = User("002", "Steve")

user_1.follow(user_2)

print(user_1.following)