users = []
gmail=[]
while True:
    user_name = str(input("user name: "))
    email_addres = str(input("email addres: "))
    password = int(input("your password: "))
    user = user_name, email_addres, password
    users.append(user)
    gmail.append(email_addres)
    exit = input("Do you want to continue?[y]|[n]: ")
    if exit == "n":
        break


def chek_gmail(gmail):
    if "@gmail" in gmail:
        return print("users",users, "isGmail= YES")
    else:
        return print("users",users, "isGmail= NO")
    
for i in gmail:
    if chek_gmail(i):
        gmail=i

        print(users)
