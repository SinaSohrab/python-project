users = []
while True:
    user_name = str(input("user name: "))
    email_addres = str(input("email addres: "))
    password = int(input("your password: "))
    user = user_name, email_addres, password
    users.append(user)
    exit = input("Do you want to continue?[y]|[n]: ")
    if exit == "n":
        break


def chek_gmail(email_addres):
    if "@gami" in email_addres:
        return print("isGmail= YES")
    else:
        return print("isGmail= NO")


print(users, chek_gmail(email_addres))
