class Heap:
    def __init__(self):
        self.cbt = []
        self.next_index = 0

    def _up_heapify(self):
        child_index = self.next_index
        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element < child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            max_element = parent

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            if left_child is not None:
                max_element = max(parent, left_child)

            if right_child is not None:
                max_element = max(right_child, max_element)

            if max_element == parent:
                return

            if max_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = left_child_index

            elif max_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = right_child_index

    def size(self):
        return self.next_index

    def insert(self, data):
        self.cbt.append(data)
        self._up_heapify()
        self.next_index += 1

    def remove(self):
        if self.size() == 0:
            return None

        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        self.cbt[0] = last_element
        self.cbt[self.next_index] = to_remove
        self._down_heapify()

        return to_remove


def rearrange_digits(input_list):
    if not input_list:
        return []

    heap = Heap()
    for item in input_list:
        heap.insert(item)

    first_number = ''
    second_number = ''

    for i in range(heap.size()):
        if i % 2 == 1:
            first_number += str(heap.remove())
        else:
            second_number += str(heap.remove())

    return [int(first_number), int(second_number)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


def test_1():
    print("Test 1: Normal case")
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    # Pass
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    # Pass


def test_2():
    print("Test 2: Other case")
    test_function([[0, 1], [1, 0]])
    # Pass
    test_function([[1, 0], [1, 0]])
    # Pass


def test_3():
    print("Test 3: Edge case")
    test_function([[1, 1], [1, 1]])
    # Pass
    test_function([[], []])
    # Pass
    test_function([[], [0, 0]])
    # Pass


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
