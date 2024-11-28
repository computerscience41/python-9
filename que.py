from collections import deque

# Initialize a queue
queue = deque()

queue.append(10)  #
queue.append(20)  


print("Dequeued element:", queue.popleft())  

# Print the queue after dequeue
print("Queue after dequeue:", list(queue))  
