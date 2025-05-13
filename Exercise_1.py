class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
  def __init__(self):
      self.stack = []
      
  def isEmpty(self):
    '''
    TC: O(1)
    AS: O(1)
    '''
    if not self.stack:
      return False
    else:
      return True
      
  def push(self, item):
    '''
    TC: O(1)
    AS: O(1)
    '''
    return self.stack.append(item)
      
  def pop(self):
    '''
    TC: O(1)
    AS: O(1)
    '''
    return self.stack.pop()
    
  def peek(self):
    '''
    TC: O(1)
    AS: O(1)
    '''
    return self.stack[-1]

  def size(self):
    '''
    TC: O(1)
    AS: O(1)
    '''
    return len(self.stack)
      
  def show(self):
    '''
    TC: O(n)
    AS: O(n)
    '''
    return self.stack

    
s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
