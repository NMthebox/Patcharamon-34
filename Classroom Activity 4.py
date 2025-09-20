import math
a = {10, 20, 30, 40, 50,60}
b = {30, 40, 50, 60, 70,80}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

loops = [
    ("range(1, 101)", range(1, 101)),
    ("range(7, 77, 7)", range(7, 77, 7)),
    ("range(20, 1, -2)", range(20, 1, -2)),
    ("range(2, 18, 3)", range(2, 18, 3)),
    ("range(55, 0, -11)", range(55, 0, -11)),
    ("range(1, 0)", range(1, 0))
