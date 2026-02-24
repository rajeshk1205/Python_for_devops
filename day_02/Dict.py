# Dict:

info = {
    "name": "Rajesh",
    "city": "Pune",
    "qualification": "B. tech",
    "Age": 26,
    "Salary": 6000.5,
    'married': False
}

print(type(info))
print(info['Age'])
print("I love: ", info.get('name'))

info.update({"Salary": 70050.0})
print(info)


for key, value in info.items():
    print(key+ " .. "+ str(value))