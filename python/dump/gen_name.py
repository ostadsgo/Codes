users = [
    "Daniel Smith",
    "Daniel Smith",
    "Ava Davis",
    "Sophia Anderson",
    "Michael Martin",
    "William Taylor",
    "Emma Smith",
    "John Anderson",
    "William Taylor",
    "William Taylor",
    "Matthew Davis",
    "Daniel Smith",
    "William Taylor",
    "Sophia Brown",
    "Olivia Taylor",
    "Daniel Smith",
]
usernames = []

for user in users:
    split_result = user.split(" ")
    first = split_result[0]
    last = split_result[1]
    username = first[0] + last[0] + last[-1]
    username = username.lower()
    usernames.append(username)

    n = usernames.count(username)
    res_un = username + str(n)
    print(user, "-", res_un)

