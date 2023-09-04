alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text,shift,direction):
    new_text=""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position=(position+shift)%26
        elif direction == "decode":
            new_position=(position-shift)%26
        new_text += alphabet[new_position]
    print(f"Here is the {direction}d result : {new_text}")
from art import logo
print(logo)
repeatatioan = 0
while repeatatioan!=1:
    user_input=input("If You Want To Continue Type yes otherwies no : \n")
    if user_input=="yes":
       direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
       text = input("Type your message:\n").lower()
       shift = int(input("Type the shift number:\n"))
       caesar(text,shift,direction)
    elif user_input=="no":
       print("Goodbye..fuck you!!!")
       repeatatioan=1

