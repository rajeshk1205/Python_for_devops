# Set()

set1 = {12}
print(type(set1))

set1 = {12,23,12,1,23,12,2,2,223,2,3,3,3}
print(set1)


num1 = [1,2,3,4,5,3,2,121,2,-2,3,4,5,3,22,2,1,2,-34]

print(num1)
num1 = list(set(num1))
print("Unique items only",num1)