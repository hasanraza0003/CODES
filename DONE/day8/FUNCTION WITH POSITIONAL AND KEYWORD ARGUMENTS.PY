# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("how are you?")
    print("have a nice day")


welcome=greet()


#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Hasan Raza")

# function with more than 1 input

def greet_with(name, location):
   print(f"hello {name}")
   print(f"how's the temperature in your area {location}")

greet_with("Hasan Raza","Uttarakhand")


# function with keyword arguments
def greet_with(name, location):
   print(f"hello {name}")
   print(f"how's the temperature in your area {location}")

greet_with(location="Uttarakhand",name="Hasan Raza")


