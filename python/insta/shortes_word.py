# joinur way of finding shortes word

words = ["hello", "hi", "salam", "merhaba"]

shortes_word = words[0]
for word in words[1:]:
    if len(word) < len(shortes_word):
        shortes_word = word

print(shortes_word)  # hi

shortest_word = min(words, key=len)
print(shortest_word)

