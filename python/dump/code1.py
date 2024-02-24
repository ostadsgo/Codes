
def say_hello(name: str) -> str:
    return f"Hello {name}"



def main():
    name: str = "John"
    print(say_hello(name))


if __name__ == "__main__":
    main()
