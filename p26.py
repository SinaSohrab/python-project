def ramz_is_ok(ramz):
    if (
        ramz_digits["se"] / ramz_digits["yek"] == 4
        and ramz_digits["chahar"] % 2 != 0
        and ramz_digits["yek"] - ramz_digits["chahar"] == 1
        and ramz_digits["se"] - ramz_digits["do"] == 3
        and ramz_digits["do"] / ramz_digits["yek"] == 2.5
    ):
        return True


for ramz in range(1000, 10000):
    this_ramz = str(ramz).zfill(4)

    ramz_digits = {}
    ramz_digits["yek"] = float(this_ramz[0])
    ramz_digits["do"] = float(this_ramz[1])
    ramz_digits["se"] = float(this_ramz[2])
    ramz_digits["chahar"] = float(this_ramz[3])

    if ramz_is_ok(ramz):
        print(ramz)