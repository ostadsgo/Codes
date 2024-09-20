def sum_of_intervals(intervals):
    total = 0
    intervals = sorted(intervals, key=lambda pair: pair[0])
    print(intervals)
    j = 1
    if len(intervals) == 1:
        x, y = intervals[0]
        return y - x

    if len(intervals) == 2:
        x, y = intervals[0]
        a, b = intervals[1]
        return y - x if (y - x) in range(a, b) else (y - x) + (b - a)

    for interval in intervals:
        for next_interval_index in range(j, len(intervals)):
            x, y = interval
            a, b = intervals[next_interval_index]
            t1 = y - x
            if t1 in range(a, b):
                total += b - x
            else:
                total += y - x
            j += 1
    print("total", total)
    return total


# print( sum_of_intervals([(1, 4), (7, 10), (3, 5), (3, 5), (2, 4)]))
assert sum_of_intervals([(1, 5)]) == 4
assert sum_of_intervals([(1, 5), (6, 10)]) == 8
assert sum_of_intervals([(1, 5), (1, 5)]) == 4
assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7
assert sum_of_intervals([(-100000000, 10), (0, 20), (30, 40)]) == 100000030
