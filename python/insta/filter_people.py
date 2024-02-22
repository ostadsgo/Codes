people = {"Mahsa": 22, "Sarina": 16, "Hadis": 23, "Nika": 17}
adults = filter(lambda item: item[1] >= 18, people.items())
print(dict(adults))

input()
