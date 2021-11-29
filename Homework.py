"""
2) Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""
from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.r = right
        self.l = left
        self.v = value


def get_the_code(root, codes=dict(), code=''):
    if root is None:
        return

    if isinstance(root.v, str):
        codes[root.v] = code
        return codes

    get_the_code(root.l, codes, code + '0')
    get_the_code(root.r, codes, code + '1')

    return codes


def tree(string):
    str_count = Counter(string)

    if len(str_count) <= 1:
        node = Node(None)

        if len(str_count) == 1:
            node.l = Node([i for i in str_count][0])
            node.r = Node(None)

        str_count = {node: 1}

    while len(str_count) != 1:
        node = Node(None)
        info = str_count.most_common()[:-3:-1]

        if isinstance(info[0][0], str):
            node.l = Node(info[0][0])

        else:
            node.l = info[0][0]

        if isinstance(info[1][0], str):
            node.r = Node(info[1][0])

        else:
            node.r = info[1][0]

        del str_count[info[0][0]]
        del str_count[info[1][0]]
        str_count[node] = info[0][1] + info[1][1]

    return [i for i in str_count][0]


def huffman_encode(string, codes):
    res = ''

    for bit in string:
        res += codes[bit]

    return res


def huffman_decode(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for c in codes:

            if string[i:].find(codes[c]) == 0:
                res += c
                i += len(codes[c])

    return res


user_text = input('Введите строку для сжатия: ')
tree = tree(user_text)

codes = get_the_code(tree)
print(f'Шифр: {codes}')

encode_str = huffman_encode(user_text, codes)
print('Сжатая строка: ', encode_str)

decode_str = huffman_decode(encode_str, codes)
print('Исходная строка: ', decode_str)
