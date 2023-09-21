with open(r"day26\file1.txt") as file:
    f1=file.readlines()

with open(r"day26\file2.txt") as file2:
    f2=file2.readlines()

result=[int(num) for num in f1 if num in f2]
print(result)