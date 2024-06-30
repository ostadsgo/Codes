import struct

import chardet


# Read file
def read_file(filename: str) -> list[bytes]:
    """Read file and reaturn its content."""
    with open(filename, "rb") as file:
        raw_data = file.read()

        return raw_data


def detect_encoding(raw_data: bytes) -> str:
    result = chardet.detect(raw_data)
    encoding = result.get("encoding")
    if encoding:
        return encoding
    return "utf-8"


def decode_data(raw_data: bytes, encoding: str) -> str:
    result = ""
    try:
        result = raw_data.decode(encoding)
    except UnicodeDecodeError as e:
        result = f"Decode Error {e}"
    return result


def main():
    raw_data = read_file("example.rsp")
    # result = struct.unpack("i", raw_data)
    print(raw_data[:4])
    print(raw_data[4:8])
    print(raw_data[8:12])
    x = raw_data[12:16]
    s = x.decode("utf-8")
    print(s)

    # for raw_chunk in raw_data[::4]:
    #     print('x')
    #     result = struct.unpack("i", raw_chunk)
    #     print(result)

    # for raw_chunk in raw_data[:100]:
    # encoding = detect_encoding(raw_chunk)
    # data = decode_data(raw_chunk, encoding)
    # print(data)
    # print(result)


if __name__ == "__main__":
    main()
