f = open("db.csv")
data = f.read().split("\n")
f.close()

city_name = input("Enter a city name: ")
data.pop()
print(city_name.capitalize())
print('---------------------')
for row in data:
    person  = row.split(',')
    first_name = person[0].capitalize()
    last_name = person[1].capitalize()
    city = person[2]
    if city.lower() == city_name.lower():
        print(f"{first_name},{last_name},{city.capitalize()}")
    
