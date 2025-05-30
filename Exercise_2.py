import math

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, data):
        '''
        TC: O(1)
        AS: O(1)
        '''
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.size = self.size + 1
        
    def pop(self):
        '''
        TC: O(1)
        AS: O(1)
        '''
        if self.head is None:
            return math.inf
        res = self.head.data
        self.head = self.head.next
        self.size = self.size - 1
        return res

        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
