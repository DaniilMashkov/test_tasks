# 1
move_zero_to_end = lambda lst: [x for x in lst if x != 0] + [x for x in lst if x == 0]


# 2
def row_sum(n: int) -> int:
    return n ** 3


assert (move_zero_to_end([1, 0, 'sc', 0, 8]) == [1, 'sc', 8, 0, 0])
assert (row_sum(6) == 216)
