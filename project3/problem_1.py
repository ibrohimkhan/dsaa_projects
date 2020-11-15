def sqrt(number: int):
    if number < 0:
        return None

    if number == 0 or number == 1:
        return number

    start = 0
    end = number

    while start < end:
        middle = (start + end) // 2
        middle_pow = middle * middle

        if middle_pow == number:
            return middle
        elif middle_pow < number:
            start = middle + 1
        else:
            end = middle - 1

    return start


def test_1():
    print("Test 1: Normal case")

    print("Pass" if (3 == sqrt(9)) else "Fail")
    # Pass
    print("Pass" if (0 == sqrt(0)) else "Fail")
    # Pass
    print("Pass" if (4 == sqrt(16)) else "Fail")
    # Pass
    print("Pass" if (1 == sqrt(1)) else "Fail")
    # Pass
    print("Pass" if (5 == sqrt(27)) else "Fail")
    # Pass


def test_2():
    print("Test 2: Zero value")

    print("Pass" if (0 == sqrt(0)) else "Fail")
    # Pass


def test_3():
    print("Test 3: Negative value")

    print("Pass" if (None == sqrt(-10)) else "Fail")
    # Pass


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()