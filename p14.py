list_name = []
list_age = []
list_city = []

while True:
    name = input("whats your name: ")
    age = input("age: ")
    city = input("What is the name of fame: ")
    if name == 0:
        break
    list_name.append(name)
    list_age.append(age)
    list_city.append(city)

print("name: ", list_name)
print("age: ", list_age)
print("city: ", list_city)
