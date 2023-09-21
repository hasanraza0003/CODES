# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# .lower()
# .count()
name=name1+name2
lowercase=name.lower()
t=lowercase.count("t")
r=lowercase.count("r")
u=lowercase.count("u")
e=lowercase.count("e")
true=int(t)+int(r)+int(u)+int(e)
l=lowercase.count("l")
o=lowercase.count("o")
v=lowercase.count("v")
e=lowercase.count("e")
love=int(l)+int(o)+int(v)+int(e)
truelove=str(true)+str(love)
if( int(truelove)<10 or int(truelove)>90):
    print(f"Your score is {truelove}, you go together like coke and mentos")
elif(int(truelove)>=40 and int(truelove)<=50):
    print(f"Your score is {truelove}, you are alright together")
else:
    print(f"Your score is {truelove}")

