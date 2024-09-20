def solution1(word):
    res = ""
    for ch in word:
        if 65 <= ord(ch) <= 90:
            res += " " + ch
        else:
            res += ch
    return res


def solution(word):
    s = ""
    for ch in word:
        if ch.isupper():
            s += " " + ch
        else:
            s += ch
    return s


assert solution("helloWorld") == "hello World"
assert solution("camelCase") == "camel Case"
assert solution("breakCamelCase") == "break Camel Case"
