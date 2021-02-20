
# coding: utf-8

# In[1]:


#reverse stack using recursion
def insertAtBottom(stack, item): 
    if isEmpty(stack): 
        push(stack, item) 
    else: 
        temp = pop(stack) 
        insertAtBottom(stack, item) 
        push(stack, temp) 
  
# Below is the function that  
# reverses the given stack 
# using insertAtBottom() 
def reverse(stack): 
    if not isEmpty(stack): 
        temp = pop(stack) 
        reverse(stack) 
        insertAtBottom(stack, temp) 
  
# Below is a complete running  
# program for testing above 
# functions. 
  
# Function to create a stack.  
# It initializes size of stack 
# as 0 
def createStack(): 
    stack = [] 
    return stack 
  
# Function to check if  
# the stack is empty 
def isEmpty( stack ): 
    return len(stack) == 0
  
# Function to push an  
# item to stack 
def push( stack, item ): 
    stack.append( item ) 
  
# Function to pop an  
# item from stack 
def pop( stack ): 
  
    # If stack is empty 
    # then error 
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
  
    return stack.pop() 
  
# Function to print the stack 
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
  
# Driver Code 
  
stack = createStack() 
push( stack, str(4) ) 
push( stack, str(3) ) 
push( stack, str(2) ) 
push( stack, str(1) ) 
print("Original Stack ") 
prints(stack) 
  
reverse(stack) 
  
print("Reversed Stack ") 
prints(stack) 


# In[2]:


# Queue reversing using recursion
class Queue: 
    def __init__(self): 
        self.items = [] 
  
  
    def isEmpty(self): 
        return self.items == [] 
  
    def add(self, item): 
        self.items.append(item) 
  
    def pop(self): 
        return self.items.pop(0) 
  
    def front(self): 
        return self.items[0] 
  
    def printQueue(self): 
        for i in self.items: 
            print(i, end =" ") 
        print("") 
  
  
# Recursive Function to reverse the queue 
def reverseQueue(q): 
  
    # Base case 
    if (q.isEmpty()): 
        return
  
    # Dequeue current item (from front)  
    data = q.front(); 
    q.pop(); 
  
    # Reverse remaining queue   
    reverseQueue(q) 
  
    # Enqueue current item (to rear)   
    q.add(data) 
  
  
# Driver Code 
q = Queue() 
q.add(56) 
q.add(27) 
q.add(30) 
q.add(45) 
q.add(85) 
q.add(92) 
q.add(58) 
q.add(80) 
q.add(90) 
q.add(100) 
reverseQueue(q) 
q.printQueue()

