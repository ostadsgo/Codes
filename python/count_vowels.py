# Diffrent way to count vowels in a string


s = "This is a line of text."
# v1
count = 0
for ch in s:
    if ch == "a" or ch == "e" or \
        ch == "i" or ch == "o" or \
        ch == "u":
        count += 1

print(count)

# v2
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)

# v3
count = 0
for vowel in "aeiou":
    count += s.count(vowel)

print(count)

# v4
count = sum(1 for ch in s if ch in "aeiou")
print(count)

# v5
count = sum(s.count(vowel) for vowel in "aeiou")
print(count)

# v6
count = sum(map(s.count, "aeiou"))
print(count)




