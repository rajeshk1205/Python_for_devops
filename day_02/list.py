# 2. Data structure:
    # 1. list
    # 2. tuple
    # 3. dict
    # 4. 

# 1. list :===============================

a = [234,12,'test',False]
a.append(100)
a.append(12.23)
a.append(True)
a.append("string values")

print(a)
print(type(a))


cloud = list()
cloud.append('Aws')
cloud.append('Azur')
cloud.append('gcp')
cloud.append('utho')
print(cloud)
print(type(cloud))


print("The total cloud platform are: ", len(cloud))
print("The first cloud platform is: ", cloud[0])

print(cloud.append.__doc__)

print("The cloud platform providers are:")
for i in cloud:
    print(" - "+i)




