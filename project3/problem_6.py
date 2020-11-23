import random


def get_min_max(ints):
    if len(ints) == 0:
        return []

    min_item = ints[0]
    max_item = ints[len(ints) - 1]

    for item in ints:
        if item <= min_item:
            min_item = item

        if item >= max_item:
            max_item = item

    return min_item, max_item


def test_1():
    print("Test 1: Normal case")
    items = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(items)

    print("Pass" if ((0, 9) == get_min_max(items)) else "Fail")
    # Pass

    items = [i for i in range(99, 135)]  # a list containing 0 - 9
    random.shuffle(items)

    print("Pass" if ((99, 134) == get_min_max(items)) else "Fail")
    # Pass


def test_2():
    print("Test 2: Empty list")
    print("Pass" if ([] == get_min_max([])) else "Fail")
    # Pass


def test_3():
    print("Test 3: With zero elements")
    print("Pass" if ((0, 0) == get_min_max([0, 0, 0, 0, 0])) else "Fail")
    # Pass


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
