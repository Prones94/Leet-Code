'''
2. Convert Binary Number in a Linked List to Integer
Example: Binary = 1100 1 --> 1 --> 0 --> 0

Steps   |     Binary      |    Value      |     Integer   |    Answer
   1            1                0             2(0) + 1          1
   2            1                1             2(1) + 1          3
   3            0                3             2(3) + 0          6
   4            0                6             2(6) + 0         12
   
'''
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None
    
class Solution:
    def get_decimal(self, head: Node):
        value = 0
        while head:
            value += (value*2) + head.value
            head = head.next
        return value
