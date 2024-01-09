n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = [5, 4, -1, 7, 8]

i = 0
j = i + 1
mx = n[0]
sum_comb = n[0]

while i <= len(n) and j <= len(n):
    comb = sum_comb + n[j]
    if comb > mx:
        mx = comb
        sum_comb = mx
        j += 1
    else:
        i += 1
        j = i + 1
        sum_comb = n[i]

print(mx)

# i   j      mx   sum_comb   comb    comb > mx  
# -------------------------------------------
# 0   1      -2     -2         -         -
#
# 0   1      -2     -2         -1       True  
# 0   2      -1     -1          1       inside if
#
# 0   2      -1     -1         -4       False
# 1   2      -1      1         -4       inside else
#
# 1   2      -1      1         -2       False
# 2   3      -1     -3         -2       inside else
#
# 2   3      -1     -3          1       True
# 2   4       1      1          1       inside if
#
# 2   4       1      1          0       False
# 3   4       1      4          0       inside else
#
# 3   4       1      4          3       True
# 3   5       3      3          3       inside if
#
# 3   5       3      3          5       True
# 3   6       5      5          5       inside if
#
# 3   6       5      5          6       True
# 3   7       6      6          6       inside if 
#
# 3   7       6      6          1       False
# 4   5       6     -1          1       inside else
#
# 4   5       6      1          1       False
# 5   6       6      2          1       inside else
# 
# 5   6       6      2          3       False
# 6   7       6      1          3       inside else
#
# 6   7       6      1         -4       False
# 7   8       6     -5         -4       inside else
#
# 7   8       6     -5         -1       False
# 8   9       6      4         -1       inside else
#
# 8   9       6      4         -1       False 


