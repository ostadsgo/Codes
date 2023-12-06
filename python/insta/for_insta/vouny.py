# def has_duplicates(s):
#     d = {}
#     for ch in s:
#         d[ch] = d.get(ch, 0) + 1

#         # if ch in d:
#         #     d[ch] = d[ch] + 1
#         # else:
#         #     d[ch] = 1

#     return d


# x = "hello world"
# res = has_duplicates(x)
# print(res)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = list(zip(*matrix))
print(transposed)
