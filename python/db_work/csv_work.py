import csv

# f = open("data.csv")
# content = f.read()
# print(content)
#
# f.close()
f = open("data.csv")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()

