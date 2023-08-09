class User:

  def __init__(self, user_id, user_name):
    self.id = user_id
    self.user_name = user_name
    self.followers = 0
    self.following = 0

  def follow(self, user):
    user.followers += 1
    self.following += 1

user_1 = User("001", "Damian")
user_2 = User("002", "Okpala")

print(user_1.id)
print(user_1.user_name)
print(user_2.id)
print(user_2.user_name)


user_1.follow(user_2)
user_1.follow(user_2)
user_2.follow(user_1)


print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)



