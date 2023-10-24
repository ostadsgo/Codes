def has_duplicates(lst):
    element_count = {}
    for elem in lst:
        if elem in element_count:
            # Perform some action if elements are equal
            element_count[elem] = element_count.get(elem, 0) + 1
        #     element_count[elem] += 1 # x += 1   x = x + 1
        # else:
        #     element_count[elem] = 1

    return element_count


x = "hello world"
res = has_duplicates(x)
print(res)
