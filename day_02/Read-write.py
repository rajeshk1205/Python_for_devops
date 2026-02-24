# Read & Write sample file

file = open("hello.txt")
print(file.read())
file.write("I'm trying to write something")
print("reading again, after writing new changes")
print(file.read())
file.close()