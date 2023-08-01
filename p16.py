number = int(input("your number: "))
def zarb(n):
    for i in range(1,n):
        j_zarb=2*i
        return j_zarb

for i in range(1,11):
    if zarb(i):
        javab=number*i
        print(number,"*",i,"=",javab)