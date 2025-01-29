
def say_hello(name: str) -> str:
    print(f"Hello {name}")
    print("something else.")



def main():
    for i in range(10):
        if i % 2 == 0:
            say_hello("John Doe")


if __name__ == "__main__":
    main()
