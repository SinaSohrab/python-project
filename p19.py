for ramz in range(100000,10000000):
    this_ramz=str(ramz).zfill(6)

    ramz_digits={}
    ramz_digits["yek"]=int(this_ramz[0])
    ramz_digits["do"]=int(this_ramz[1])
    ramz_digits["se"]=int(this_ramz[2])
    ramz_digits["chahar"]=int(this_ramz[3])
    ramz_digits["panj"]=int(this_ramz[4])
    ramz_digits["shish"]=int(this_ramz[5])

    print(ramz_digits)