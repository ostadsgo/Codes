alph = 'abcdefghijklmnopqrstuvwxyz'
word = "uryyb jbeyq"  # hello world
res = ""
for ch in word:
    if ch in alph:
        index = alph.find(ch) + 13
        if index > len(alph):
            n = index - len(alph)
            res += alph[n]
        else:
            res += alph[index]
    else:
        res += ch
    
print(res)
