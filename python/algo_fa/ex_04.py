t = int(input("Enter time: "))
h = t // 3600
print(h)
r = t - (3600 * h)
m = r // 60
print(m)
s = r - (m * 60)
print(s)

