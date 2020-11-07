import heapq
import sys


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if other is None:
            return False

        if not isinstance(other, Node):
            return False

        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, Node):
            return False

        return self.char == other.char

    def __repr__(self):
        return f"{self.char}: {self.freq}"


def get_frequency(text):
    frequency = {}
    for char in text:
        if not char in frequency:
            frequency[char] = 0
        frequency[char] += 1

    return frequency


def create_heap(frequency):
    heap = []
    for key in frequency:
        node = Node(key, frequency[key])
        heapq.heappush(heap, node)

    return heap


def merge_nodes(heap):
    while len(heap) > 1:
        first_node = heapq.heappop(heap)
        second_node = heapq.heappop(heap)

        freq_sum = first_node.freq + second_node.freq
        merged_node = Node(None, freq_sum)
        merged_node.left = first_node
        merged_node.right = second_node

        heapq.heappush(heap, merged_node)


def binaryze(heap):
    root = heapq.heappop(heap)
    codes = {}
    byte_codes = ''

    def add_binary_code(root, byte_codes):
        if root is None:
            return

        if root.char is not None:
            codes[root.char] = byte_codes
            return

        add_binary_code(root.left, byte_codes + '0')
        add_binary_code(root.right, byte_codes + '1')

    add_binary_code(root, byte_codes)
    return codes


def reverse(codes):
    reversed_codes = {}
    for key in codes:
        reversed_codes[codes[key]] = key

    return reversed_codes


def huffman_encoding(data):
    if not data or not data.strip():
        return None, None

    freq = get_frequency(data)
    heap = create_heap(freq)
    merge_nodes(heap)

    codes = binaryze(heap)
    encoded_text = ''
    for char in data:
        encoded_text += codes[char]

    return encoded_text, codes


def huffman_decoding(data, tree):
    byte_codes = ''
    decoded_text = ''

    reverse_codes = reverse(tree)
    for bit in data:
        byte_codes += bit
        if byte_codes in reverse_codes:
            char = reverse_codes[byte_codes]
            decoded_text += char
            byte_codes = ''

    return decoded_text


def test_1():
    print("test 1: Normal case")

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word


def test_2():
    print("test 2: Edge case with empty text")
    a_great_sentence = ''

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 49
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is:

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if not encoded_data and not tree:
        print("success: data not encoded")
        # success: data not encoded


def test_3():
    print("test 2: Edge case with whitespace")
    a_great_sentence = ' '

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 50
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is:

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if not encoded_data and not tree:
        print("success: data not encoded")
        # success: data not encoded


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()