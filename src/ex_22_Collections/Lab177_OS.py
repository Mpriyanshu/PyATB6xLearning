import os

print(os.getcwd())
full_path = os.path.join(os.getcwd(), "priyanshu.txt")
#full_path = os.path.join(r"C:\Users\Abc\PycharmProjects\PyATB6xLearning\src\ex_22_Collections","priyanshu.txt")
print(full_path)

file = open(full_path, 'r')
print(file.read())