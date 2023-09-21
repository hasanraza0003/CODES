print("Welcome to the secret auction program")

details={}


signal=0

while signal != 1:
    user_input=input("Are there any other bidders ? Type 'yes' or 'no'")
    if user_input=="yes":
        name=input("what is your name? : ")
        bid=input("what is your bid? : $")
        details[name]=bid    
    elif user_input=="no":
        signal=1
   

print(f"The winner is {max(details)}")