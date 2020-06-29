import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return (None, None)
    small = float('inf')
    large = float('-inf')
    for x in ints:
        small = min(x, small)
        large = max(x, large)

    return (small, large)


# Test Case
l1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l1)
print("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")

l2 = [3, 3, 3, 3]
print("Pass" if ((3, 3) == get_min_max(l2)) else "Fail")

l3 = []
print("Pass" if ((None, None) == get_min_max(l3)) else "Fail")

l4 = [1]
print("Pass" if ((1, 1) == get_min_max(l4)) else "Fail")
