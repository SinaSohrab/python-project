name = input("inter your name: ")


with open("files.txt", "a") as file:
    file.write(f"{name}\n")
