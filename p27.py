class User:
    def __init__(self, user_name, pass_word, full_name):
        self.user_name = user_name
        self.pass_word = pass_word
        self.full_name = full_name

    def p(self):
        print(self.user_name,self.pass_word,self.full_name)


for i in range(0,1):
    name=input("whats your name: ")
    password=input("whats your password: ")
    fullname=input("whats your full name: ")
    user=User(name,password,fullname)


print(User)
