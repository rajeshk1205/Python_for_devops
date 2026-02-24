# for loop

for i in range(1, 11):
    print(i)


# Odd/Even number:
for i in range(1, 11):
    if i%2 == 0:
        print("Ever number: ",i)
    else:
        print("Odd number: ",i)

for i in range(5):
    env = input("Enter a value for env: ")
    print("The entered value  is: ", env)

    if env == "prod":
        print("Do not release any changes on Friday")
    elif env == "dev":
        print("Release this, in office Network only and test well.")
    elif env == "test":
        print("Can make the release any-time")
    else:
        print("Did not match the env values, please try again.")