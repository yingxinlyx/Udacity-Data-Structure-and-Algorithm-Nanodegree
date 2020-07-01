def desc_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = desc_sort(arr[0:mid])
    right = desc_sort(arr[mid:])
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return [0, 0]
    sorted = desc_sort(input_list)
    res = ['0', '0']
    for i in range(len(sorted)):
        idx = i % 2
        res[idx] += str(sorted[i])

    return [int(res[0]), int(res[1])]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 1, 0], [10, 0]])
test_function([[], [0, 0]])
test_function([None, [0, 0]])
