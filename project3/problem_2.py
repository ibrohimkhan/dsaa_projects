def recursive_search(input_list, number, start, end):
    if start > end:
        return -1

    middle = (start + end) // 2
    if input_list[middle] == number:
        return middle

    left = recursive_search(input_list, number, start, middle - 1)
    if input_list[left] == number:
        return left

    right = recursive_search(input_list, number, middle + 1, end)
    if input_list[right] == number:
        return right

    return -1


def rotated_array_search(input_list: list, number: int):
    return recursive_search(input_list, number, 0, len(input_list) - 1)


def linear_search(input_list: list, number: int):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def test_1():
    print("Test 1: Normal case")

    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    # Pass
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    # Pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 3])
    # Pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 7])
    # Pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    # Pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    # Pass
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    # Pass
    test_function([[6, 7, 8, 9, 11, 12, 13, 1, 2, 3, 4, 5], 9])
    # Pass
    test_function([[1, 2, 3, 4, 5, 6, 7, 13, 12, 11, 10, 8], 10])
    # Pass


def test_2():
    print("Test 2: Sorted array")

    test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], 9])
    # Pass
    test_function([[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13], 10])
    # Pass


def test_3():
    print("Test 3: Empty array")

    test_function([[], 1])
    # Pass


def test_4():
    print("Test 4: Array with one element")

    test_function([[1], 0])
    # Pass


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()