import sys
from collections import Counter, namedtuple
import heapq

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc+"0")
        self.right.walk(code, acc+"1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char]=acc or '0'

def huffman_decode(code, encoded):
    code={dig: let for let, dig in code.items()}
    cur=''
    res=''
    for digit in encoded:
        cur+=digit
        if cur in code:
            res+=code[cur]
            cur=''
    return res

def huffman_encode(s):
    heap=[]
    for ch, freq in Counter(s).items():
        heap.append((freq, len(heap), Leaf(ch)))
    heapq.heapify(heap)
    count=len(heap)
    while len(heap)>1:
        freq1, _count1, left=heapq.heappop(heap)
        freq2, _count2, right=heapq.heappop(heap)
        heapq.heappush(heap, (freq2+freq1, count, Node(left, right)))
        count+=1
    code={}
    if heap:
        [(_freq, _count, root)]=heap
        root.walk(code, "")
    return code

def main():
    s=sys.stdin.readline().strip()
    code=huffman_encode(s)
    encoded="".join(code[ch] for ch in s)
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)
    print(huffman_decode(code, encoded))

def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length=random.randint(0, 32)
        s="".join(random.choice(string.ascii_letters) for _ in range(length))
        code=huffman_encode(s)
        encoded="".join(code[ch] for ch in s)
        decoded=huffman_decode(code, encoded)
        assert s==decoded
        print('ok')

if __name__ == '__main__':
    test()


