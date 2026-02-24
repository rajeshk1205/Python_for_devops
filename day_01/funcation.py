#function in python

def sum_of_numbers():   # function definition
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

env = input("Enter a value for env: ")
print("The entered value  is: ", env)
if env == "Prod":
    sum_of_numbers()     #function calling