randnum = "123"

guess = "110"

d1, d2, d3 = randnum
e1, e2, e3 = guess
res = ""
if e1 not in randnum and e2 not in randnum and e3 not in randnum:
    print("Bagles")
    
i = -1
for e in guess:
    i += 1
    if e == randnum[i]:
        res += "Fermi "
        continue
    if e in randnum:
        res += "Pico "
    
    
print(res)
