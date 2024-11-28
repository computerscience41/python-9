from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"

    def is_empty(self):
        return not self.stack


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)

    print("Peek:", stack.peek())  
    print("Pop:", stack.pop())    
    print("Peek after pop:", stack.peek())  
    print("Stack empty:", stack.is_empty()) 
