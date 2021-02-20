
# coding: utf-8

# In[4]:


#left view
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
# Recursive function pritn left view of a binary tree
def leftViewUtil(root, level, max_level):
     
    # Base Case
    if root is None:
        return
 
    # If this is the first node of its level
    if (max_level[0] < level):
        print ("% d\t" %(root.data))
        max_level[0] = level
 
    # Recur for left and right subtree
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)
 
 
# A wrapper over leftViewUtil()
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)
 
 
# Driver program to test above function
root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
 
leftView(root)


# In[6]:


#right view
class Node: 
    # A constructor to create a new Binary tree Node 
    def __init__(self, item): 
        self.data = item 
        self.left = None
        self.right = None
      
# Recursive function to print right view of Binary Tree 
# used max_level as reference list ..only max_level[0]  
# is helpful to us 
def rightViewUtil(root, level, max_level): 
      
    # Base Case 
    if root is None: 
        return
      
    # If this is the last node of its level 
    if (max_level[0] < level): 
        print ("%d   " %(root.data)) 
        max_level[0] = level 
  
    # Recur for right subtree first, then left subtree 
    rightViewUtil(root.right, level+1, max_level) 
    rightViewUtil(root.left, level+1, max_level) 
  
def rightView(root): 
    max_level = [0] 
    rightViewUtil(root, 1, max_level) 
  
  
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
  
rightView(root) 


# In[7]:


#top view
class newNode: 
 
    # Construct to create a newNode 
    def __init__(self, key): 
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0
 
# function should print the topView 
# of the binary tree 
def topview(root) :
 
    if(root == None) :
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd 
 
    # push node and horizontal
    # distance to queue 
    q.append(root) 
 
    while(len(q)) :
        root = q[0]
        hd = root.hd 
         
        # count function returns 1 if the 
        # container contains an element 
        # whose key is equivalent to hd, 
        # or returns zero otherwise. 
        if hd not in m:
            m[hd] = root.data 
        if(root.left) :         
            root.left.hd = hd - 1
            q.append(root.left) 
         
        if(root.right):         
            root.right.hd = hd + 1
            q.append(root.right) 
         
        q.pop(0)
    for i in sorted (m):
        print(m[i], end = "") 
 
# Driver Code 
if __name__ == '__main__':
 
    """ Create following Binary Tree 
         1 
        / \ 
        2 3 
        \ 
          4 
           \ 
            5 
             \ 
                6*"""
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.right = newNode(4) 
    root.left.right.right = newNode(5) 
    root.left.right.right.right = newNode(6) 
    print("Following are nodes in top", 
          "view of Binary Tree") 
    topview(root)


# In[8]:


#bottom view
class Node: 
      
    def __init__(self, key): 
          
        self.data = key 
        self.hd = 1000000
        self.left = None
        self.right = None
   
# Method that prints the bottom view. 
def bottomView(root): 
  
    if (root == None): 
        return
      
    # Initialize a variable 'hd' with 0 
    # for the root element. 
    hd = 0
      
    # TreeMap which stores key value pair 
    # sorted on key value 
    m = dict() 
   
    # Queue to store tree nodes in level 
    # order traversal 
    q = [] 
   
    # Assign initialized horizontal distance 
    # value to root node and add it to the queue. 
    root.hd = hd 
      
    # In STL, append() is used enqueue an item 
    q.append(root)   
   
    # Loop until the queue is empty (standard 
    # level order loop) 
    while (len(q) != 0): 
        temp = q[0] 
          
        # In STL, pop() is used dequeue an item 
        q.pop(0)   
          
        # Extract the horizontal distance value 
        # from the dequeued tree node. 
        hd = temp.hd 
   
        # Put the dequeued tree node to TreeMap 
        # having key as horizontal distance. Every 
        # time we find a node having same horizontal 
        # distance we need to replace the data in 
        # the map. 
        m[hd] = temp.data 
   
        # If the dequeued node has a left child, add 
        # it to the queue with a horizontal distance hd-1. 
        if (temp.left != None): 
            temp.left.hd = hd - 1
            q.append(temp.left) 
   
        # If the dequeued node has a right child, add 
        # it to the queue with a horizontal distance 
        # hd+1. 
        if (temp.right != None): 
            temp.right.hd = hd + 1
            q.append(temp.right) 
   
    # Traverse the map elements using the iterator. 
    for i in sorted(m.keys()): 
        print(m[i], end = ' ') 
          
# Driver Code 
if __name__=='__main__': 
      
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22) 
    root.left.left = Node(5) 
    root.left.right = Node(3) 
    root.right.left = Node(4) 
    root.right.right = Node(25) 
    root.left.right.left = Node(10) 
    root.left.right.right = Node(14) 
      
    print("Bottom view of the given binary tree :") 
      
    bottomView(root) 

