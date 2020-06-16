import sys
from collections import defaultdict
from pprint import pprint
import heapq
import inspect


class Node:
    def __init__(self, *args, value=None, chars = None):
        self.value = value
        self.chars = chars
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __repr__(self):
        return f'Node({self.value}, char = {self.chars})'

class Tree:
    def __init__(self, root):
        self.root = root
    
    def traverse_in_order(self):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            pprint(node)
            traverse(node.right)
        
        traverse(self.root)
    
    def size(self):
        def traverse(node):
            if not node:
                return 0
            return 1 + traverse(node.left) + traverse(node.right)
        num = traverse(self.root)
        return num
    
    def encode_char(self, char):
        rep = ""
        if self.size() == 1:
            #for exception case where only 1 node exists(if string passed is all 1 characters)
            return '1'
        node = self.root
        while True:
            if node is None:
                break
            elif node.chars[0] == char and len(node.chars) == 1:
                break
            elif char in node.left.chars:
                rep+="0"
                node = node.left
            elif char in node.right.chars:
                rep+="1"
                node = node.right
        return rep
    
    def decode_str(self, data:str):
        if self.size() == 1:
            return self.root.chars[0]*len(data)
        curr_node:Node = self.root
        output = ""
        i = 0
        max_len = len(data)
        while True:
            if len(curr_node.chars) == 1:
                output+=curr_node.chars[0]
                curr_node = self.root
                continue
            if i>=max_len:
                break
            elif int(data[i]) == 0:
                curr_node = curr_node.left
            elif int(data[i]) == 1:
                curr_node = curr_node.right
            i+=1
        return output

def huffman_encoding(data:str):
    if not data:
        return None, None
    freq = defaultdict(lambda: 0)
    for char in data:
        freq[char] +=1
    minheap = []
    for key,item in freq.items():
        heapq.heappush(minheap, Node(value=item, chars = key))
    
    while len(minheap) > 1:
        left = heapq.heappop(minheap)
        right = heapq.heappop(minheap)

        interm = Node(value = left.value+right.value, chars = left.chars + right.chars)
        interm.left = left
        interm.right = right

        heapq.heappush(minheap, interm)
    tree = Tree(minheap[0])

    map = {}
    for key, item in freq.items():
        repr = tree.encode_char(key)
        map[key] = repr

    encoded = ""
    for char in data:
        encoded+=map.get(char)
    
    return encoded, tree

def huffman_decoding(data,tree:Tree):
    if not data or not tree:
        return None
    return tree.decode_str(data)

def test_1():
    '''Sentence from Udacity problem description '''
    print("Excecuting {}".format(inspect.stack()[0].function))
    sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    encoded, tree = huffman_encoding(sentence)
    decoded = huffman_decoding(encoded, tree)
    print(f'Sentence to be encoded: \n {sentence}')
    print(f'Encoded sentence: \n {encoded}')
    print(f'Decoded sentence: \n {decoded}')
    assert sentence == decoded, print(f'{sentence} =/= {decoded}')

def test_2():
    '''Sentence with spaces'''
    print("Excecuting {}".format(inspect.stack()[0].function))
    sentence = "The bird is the word"
    encoded, tree = huffman_encoding(sentence)
    decoded = huffman_decoding(encoded, tree)
    print(f'Sentence to be encoded: \n {sentence}')
    print(f'Encoded sentence: \n {encoded}')
    print(f'Decoded sentence: \n {decoded}')
    assert sentence == decoded, print(f'{sentence} =/= {decoded}')

def test_3():
    '''Sentence w/ numbers'''
    print("Excecuting {}".format(inspect.stack()[0].function))
    sentence = '125 North Mary Avenue'
    encoded, tree = huffman_encoding(sentence)
    decoded = huffman_decoding(encoded, tree)
    print(f'Sentence to be encoded: \n {sentence}')
    print(f'Encoded sentence: \n {encoded}')
    print(f'Decoded sentence: \n {decoded}')
    assert sentence == decoded, print(f'{sentence} =/= {decoded}')

def test_4():
    print("Excecuting {}".format(inspect.stack()[0].function))
    sentence = '' # in python empty string is falsy
    encoded, tree = huffman_encoding(sentence)
    decoded = huffman_decoding(encoded, tree)
    print(f'Sentence to be encoded: \n {sentence}')
    print(f'Encoded sentence: \n {encoded}')
    print(f'Decoded sentence: \n {decoded}')
    assert decoded == None, print(f'{sentence} =/= {decoded}')

def test_5():
    '''Sentence w/ numbers'''
    print("Excecuting {}".format(inspect.stack()[0].function))
    sentence = 'aaaaaaa'
    encoded, tree = huffman_encoding(sentence)
    decoded = huffman_decoding(encoded, tree)
    print(f'Sentence to be encoded: \n {sentence}')
    print(f'Encoded sentence: \n {encoded}')
    print(f'Decoded sentence: \n {decoded}')
    assert sentence == decoded, print(f'{sentence} =/= {decoded}')

if __name__ == "__main__":


    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()