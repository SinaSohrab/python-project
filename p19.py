def ramz_is_okey(ramz_digits):
    if (
        ramz_digits["yek"] == ramz_digits["panj"]
        and (ramz_digits["yek"] * 2)+1 == ramz_digits["do"]
        and (ramz_digits["panj"] / 2) == ramz_digits["chahar"]
        and (ramz_digits["yek"] - 1) == ramz_digits["shish"]
        and (ramz_digits["se"] * 4)+1
        == ramz_digits["yek"]
        + ramz_digits["do"]
        + ramz_digits["se"]
        + ramz_digits["chahar"]
        + ramz_digits["panj"]
        + ramz_digits["shish"]
    ):
        return True


for ramz in range(100000, 1000000):
    this_ramz = str(ramz).zfill(6)

    ramz_digits = {}
    ramz_digits["yek"] = int(this_ramz[0])
    ramz_digits["do"] = int(this_ramz[1])
    ramz_digits["se"] = int(this_ramz[2])
    ramz_digits["chahar"] = int(this_ramz[3])
    ramz_digits["panj"] = int(this_ramz[4])
    ramz_digits["shish"] = int(this_ramz[5])

    if ramz_is_okey(ramz_digits):
        print(ramz)
