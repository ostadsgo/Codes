from collections import deque



q = deque([1, 2, 3, 4, 5])
q.append(6)

q.popleft()

q.extendleft(["hello", "a", "b"])  # Append to the q from right element to left element 

q.popleft()

print(q)


