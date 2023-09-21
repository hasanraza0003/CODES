#creating a class

class User():
	
# constructing attribue
	def __init__(self,user_id,username):
		self.id=user_id
		self.username= username
		self.follower= 0
		self.following=0

#constructing a method
	def follow(self, user):
		user.follower +=1
		self.following +=1 


# calling attributes
user_1=User("001","Hasan")
user_2=User("002","Raza")

print (user_1.username)
print(user_2.username)


# calling methods
user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)


