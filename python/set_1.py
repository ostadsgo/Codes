s = "aaabbbcccaaa"

for ch in set(s):
    count = s.count(ch)
    print(ch, ":", count)
