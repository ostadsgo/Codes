from math import sqrt


upper_chars = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
lower_chars = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
numbers = "0 1 2 3 4 5 6 7 8 9 "
symboles = "! @ # $ % ^ & * ( ) { } / . , < > ? ; ' : ' ` = - | >> << "
alike = "o0O8 iIl1 9gqCGQ += -= *= /= -> ---> => ===> <= >= |> || <| == === != "


def max_prime_factor(n: int) -> int:
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n >>= 2

    for i in range(3, int(sqrt(n) + 1), 2):
        while n % i == 0:
            max_prime = 1
            n = n / i

    if n > 2:
        max_prime = n

    return int(max_prime)


def test():
    questions = [15, 19, 11, 17, 73, 44, 38, 28, 90, 59, 83]
    results = [5, 19, 11, 17, 73, 11, 1, 7, 5, 59, 83]
    for q, r in zip(questions, results):
        assert max_prime_factor(q) == r
        print("✅ Test passed.")


if __name__ == "__main__":
    test()
