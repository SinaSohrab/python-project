name = input("inter your name: ")
file = open("files.txt", "a")

file.write(name + "\n")
file.close()
