class User:
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password

    def Print(self):
        print(self.user_name, self.email)

    def Chek_Email(self):
        return self.email.endswith("@gmail.com")


users = []
while True:
    user_name = str(input("user name: "))
    email_addres = str(input("email addres: "))
    password = int(input("your password: "))
    user = User(user_name, email_addres, password)
    users.append(user)
    user.Chek_Email()

    exit = input("Do you want to continue?[y]|[n]: ")
    if exit == "n":
        break

print("All users: ", len(users))
for user in users:
    print("isgmail:", "Yes" if user.Chek_Email() else "No",)
