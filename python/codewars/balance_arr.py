def get_num_of_elm(arr):
    u = set(arr)
    return sorted([arr.count(item) for item in u])


def balance(arr1, arr2):
    x = get_num_of_elm(arr1)
    y = get_num_of_elm(arr2)
    return x == y


array1 = ["a", "b", "c", "d", "e", "f", "g", "g"]
print(get_num_of_elm(array1))


array1 = ["a", "b", "c", "d", "e", "f", "g", "g"]
array2 = ["h", "h", "i", "j", "k", "l", "m", "n"]
assert balance(array1, array2) == True

array1 = ["a", "b", "c", "d", "e", "f", "g", "g"]
array2 = ["h", "h", "i", "j", "k", "l", "m", "m"]
assert balance(array1, array2) == False
