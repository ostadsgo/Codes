def validate(ip):
    ip_sections = ip.split(".")
    if len(ip_sections) < 4:
        return False

    for section in ip_sections:
        if int(section) not in range(256):
            return False
        
    return True




assert validate("127.0.0.1") == True
assert validate("255.255.255.255") == True
assert validate("1.1.1.1") == True
assert validate("10.1.1") == False
assert validate("1.1.1.1000") == False
print("All tests passed")
