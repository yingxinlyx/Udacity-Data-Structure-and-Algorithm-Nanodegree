def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # invalid input
    if number < 0:
        return -1

    low = 0
    high = number
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square == number:
            return mid
        elif square > number:
            high = mid - 1
        else:
            low = mid + 1
    return high


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (-1 == sqrt(-5)) else "Fail")
print("Pass" if (10000000000 == sqrt(100000000000000000008)) else "Fail")
