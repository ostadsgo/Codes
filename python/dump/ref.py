def something(num, my_list):
    print("num id", id(num), "my_list id", id(my_list))
    num = 3
    my_list[0] = 3
    print()
    print("*** After manipulating num and my_list ***")
    print("num id", id(num), "my_list id", id(my_list))


a = 2
b = [2]

print("id a", id(a), "id b", id(b))

something(a, b)
print()
print("*** After execuate somthing(a, b) ***")
print("id a", id(a), "id b", id(b))

print(a)
print(b)
