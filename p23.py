def Print():
    print(user_name, email_addres)


def Is_Gmail():
    email_addres = email_addres.split("@gamil")

email_addres="dsag@gamil.com"
if Is_Gmail:
    print(email_addres)

users = []
while True:
    user_name = input("user name: ")
    email_addres = input("email addres: ")
    password = input("your password: ")
    user = user_name, email_addres, password
    users.append(user)
    exit = input("Do you want to continue?[y]|[n]: ")
    if exit == "n":
        break

print(users)
