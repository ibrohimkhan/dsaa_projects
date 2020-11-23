def sort_012(input_list):
    left_index = 0
    right_index = len(input_list) - 1
    current_index = 0

    while current_index <= right_index:
        if input_list[current_index] == 0:
            input_list[current_index] = input_list[left_index]
            input_list[left_index] = 0
            left_index += 1
            current_index += 1

        elif input_list[current_index] == 2:
            input_list[current_index] = input_list[right_index]
            input_list[right_index] = 2
            right_index -= 1

        else:
            current_index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    # Pass
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    # Pass
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    # Pass
