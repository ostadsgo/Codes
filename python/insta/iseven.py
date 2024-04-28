# is it even
def iseven(n):
    return n % 2


def iseven2(n):
    if n % 2 == 0:
        return True
    else:
        return False

def iseven3(n: int) -> bool:
    return [False, True][n % 2]

def main():
    # this is the main function
    iseven(1)



if __name__ == "__main__":
    pass
