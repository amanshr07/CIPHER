
# coding: utf-8

# In[2]:


#implementing stack using linked list
class Node:
     
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
     
    # head is default NULL
    def __init__(self):
        self.head = None
     
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    # Method to add data to the stack
    # adds to the start of the stack
    def push(self,data):
         
        if self.head == None:
            self.head=Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
     
    # Remove element that is the current head (start of the stack)
    def pop(self):
         
        if self.isempty():
            return None
             
        else:
            # Removes the head node and makes 
            #the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
     
    # Returns the head node data
    def peek(self):
         
        if self.isempty():
            return None
             
        else:
            return self.head.data
     
    # Prints out the stack     
    def display(self):
         
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
         
        else:
             
            while(iternode != None):
                 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return
         
# Driver code
MyStack = Stack()
 
MyStack.push(11) 
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)
 
# Display stack elements 
MyStack.display()
 
# Print top element of stack 
print("\nTop element is ",MyStack.peek())
 
# Delete top elements of stack 
MyStack.pop()
MyStack.pop()
 
# Display stack elements
MyStack.display()
 
# Print top element of stack 
print("\nTop element is ", MyStack.peek())


# In[3]:


#implementing queue using linked list
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a queue 
  
# The queue, front stores the front node 
# of LL and rear stores the last node of LL 
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
  
# Driver Code 
if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(10) 
    q.EnQueue(20) 
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(30) 
    q.EnQueue(40) 
    q.EnQueue(50)  
    q.DeQueue()    
    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data)) 


# In[4]:


#implementing stack using array
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)


# In[5]:


#implementing queue using array
class Queue: 
  
    # __init__ function 
    def __init__(self, capacity): 
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity 
        self.capacity = capacity 
      
    # Queue is full when size becomes 
    # equal to the capacity  
    def isFull(self): 
        return self.size == self.capacity 
      
    # Queue is empty when size is 0 
    def isEmpty(self): 
        return self.size == 0
  
    # Function to add an item to the queue.  
    # It changes rear and size 
    def EnQueue(self, item): 
        if self.isFull(): 
            print("Full") 
            return
        self.rear = (self.rear + 1) % (self.capacity) 
        self.Q[self.rear] = item 
        self.size = self.size + 1
        print("% s enqueued to queue"  % str(item)) 
  
    # Function to remove an item from queue.  
    # It changes front and size 
    def DeQueue(self): 
        if self.isEmpty(): 
            print("Empty") 
            return
          
        print("% s dequeued from queue" % str(self.Q[self.front])) 
        self.front = (self.front + 1) % (self.capacity) 
        self.size = self.size -1
          
    # Function to get front of queue 
    def que_front(self): 
        if self.isEmpty(): 
            print("Queue is empty") 
  
        print("Front item is", self.Q[self.front]) 
          
    # Function to get rear of queue 
    def que_rear(self): 
        if self.isEmpty(): 
            print("Queue is empty") 
        print("Rear item is",  self.Q[self.rear]) 
  
  
# Driver Code 
if __name__ == '__main__': 
  
    queue = Queue(30) 
    queue.EnQueue(10) 
    queue.EnQueue(20) 
    queue.EnQueue(30) 
    queue.EnQueue(40) 
    queue.DeQueue() 
    queue.que_front() 
    queue.que_rear() 

