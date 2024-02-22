def rgb(r, g, b):
    print(
        "".join(
            [str(hex(r))[2:].upper(), str(hex(g))[2:].upper(), str(hex(b))[2:].upper()]
        )
    )

    return "".join(
        [str(hex(r))[2:].upper(), str(hex(g))[2:].upper(), str(hex(b))[2:].upper()]
    )


print(rgb(0, 0, 0))
# assert rgb(0, 0, 0) == "000000", "testing zero values"
# assert rgb(1, 2, 3) == "010203", "testing near zero values"
assert rgb(255, 255, 255) == "FFFFFF", "testing max values"
assert rgb(254, 253, 252) == "FEFDFC", "testing near max values"
assert rgb(-20, 275, 125) == "00FF7D", "testing out of range values"
