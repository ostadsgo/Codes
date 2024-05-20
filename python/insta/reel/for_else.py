n = 7

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break

else:  # no break
    print(f"{n} is a prime number.")
