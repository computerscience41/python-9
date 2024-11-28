from collections import deque

# Create a stack using deque
stack = deque()

stack.append(10)  
stack.append(20)  

print("Peek:", stack[-1])  


print("Pop:", stack.pop()) 

print("Peek after pop:", stack[-1])
 
