# list comprehension
# * integars
numbers = [1,2,3]
new_list = [ n+1 for n in numbers]
print(new_list)


# * characters 
name = "Angela"
list = [letter for letter in name ]
print(list)

# range function 
range_list = [num*2 for num in range(1,5) ]
print(range_list)

# conditional comprehension  ---  if (test)   =>
names= ["Alex", "Beth" , "Caroline" , "Dave" ,"Elanor" , "Freddie" ]
short_names = [name for name in names if len(name)<5]
long_name = [name.upper() for name in names if len(name)>4]
print(short_names)
print(long_name)