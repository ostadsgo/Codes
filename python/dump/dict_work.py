
d = {"d": 2, "a": 1, "c": 3, "b":2 }

max_value = 0
sorted_by_value_dict = {}

for k, v in d.items():
    for value in d.values()[1:]:
        if v > value:
            sorted_by_value_dict[k] = v




