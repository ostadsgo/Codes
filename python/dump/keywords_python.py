def is_keyword(keyword: str, keywords: list[str]) -> bool:
    """Returns True if keyword is in keywords list otherwise returns Flase"""
    return keyword in keywords


def main():
    keywords = [
        "False",
        "await",
        "else",
        "import",
        "pass",
        "None",
        "break",
        "except",
        "in",
        "raise",
        "True",
        "class",
        "finally",
        "is",
        "return",
        "and",
        "continue",
        "for",
        "lambda",
        "try",
        "as",
        "def",
        "from",
        "nonlocal",
        "while",
        "assert",
        "del",
        "global",
        "not",
        "with",
        "async",
        "elif",
        "if",
        "or",
        "yield",
    ]

    keywords_to_check = ["type", "match", "case"]
    for keyword in keywords_to_check:
        assert is_keyword(keyword, keywords), f"{keyword} is not a keyword"


if __name__ == "__main__":
    main()
