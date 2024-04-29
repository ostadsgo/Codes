
def say_hello(name: str) -> str:
    return f"Hello {name}"

names = ["Joe", "Albert", "Bob"]

x = 0
if x > 0:
    print("something")
elif x < 0:
    print("Another thing.")
else:
    print("Nothing")

print(max(names, key=len))
print(min(names, key=len))
