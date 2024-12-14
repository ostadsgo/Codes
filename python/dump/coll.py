def foreach(fn, data):
    res = []
    for item in data:
        r = fn(item)
        res.append(r)
    return res
