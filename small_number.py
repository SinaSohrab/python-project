number = 95318
number_list = []
number = str(number)
for i in number:
    number_list.append(i)

number_list.sort()

sum = ""
sum = str(sum)

for i in number_list:
    sum += i

print(sum)
