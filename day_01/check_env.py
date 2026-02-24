# Get the env value from the user and print it

env = input("Enter a value for env: ")
print("The entered value  is: ", env)
print(type(env))


# if/else condition
# ==, !=, <, >, <=, >=
if env == "prod":
    print("Do not release any changes on Friday")
elif env == "dev":
    print("Release this, in office Network only and test well.")
else:
    print("We can do this anytime.")


# ==============================================================================================
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

print("a+b is: ", a+b)
print("a-b is: ", a-b)
print("a*b is: ", a*b)
print("a/b is: ", a/b)