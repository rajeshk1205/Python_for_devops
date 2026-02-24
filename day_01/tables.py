# print the table of entered number

num = int(input("Enter a number: "))
for i in range(1,  11):
    print(f"{i} * {num}: ", i*num)



Name = "Rj"
while Name == "Rj":
    num = int(input("Enter a number: "))
    print(f"You are wining amount of {num} rupees.")
    break
else:
    print(" Name is not matching..")


choise = input("Enter a choice: (press q to quit): ")
while choise != "q":
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{i} * {num}: ", i * num)
    choise = input("Enter a choice: (press q to quit): ")
