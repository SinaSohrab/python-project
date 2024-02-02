names_list = []
with open("files.txt") as file:
    for line in file:
        names_list.append(line.rstrip())

# sorted = moratab kardan az kochik be bozorg.
# reverse=True = motatab az bozorg be kochik.
# sort(item, reverse = True) z to a.
# sort(item, reverse = False) a to z.
for name in sorted(names_list):
    print(f"Hello, {name}")
