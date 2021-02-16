
# coding: utf-8

# In[12]:


class Node:  
    def __init__(self, d): 
        self.data = d 
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None
          
    # A utility function to create 
    # a new node  
    def newNode(self, key):  
        temp = Node(key)  
        self.next = None
        return temp  
  
    # Rearranges given linked list  
    # such that all even positioned  
    # nodes are before odd positioned.  
    # Returns new head of linked List.  
    def rearrangeEvenOdd(self, head):  
          
        # Corner case  
        if (self.head == None):  
            return None
  
        # Initialize first nodes of  
        # even and odd lists  
        odd = self.head  
        even = self.head.next
  
        # Remember the first node of even list so  
        # that we can connect the even list at the  
        # end of odd list.  
        evenFirst = even  
  
        while (1 == 1):  
              
            # If there are no more nodes,  
            # then connect first node of even  
            # list to the last node of odd list  
            if (odd == None or even == None or 
                              (even.next) == None):  
                odd.next = evenFirst  
                break
  
            # Connecting odd nodes  
            odd.next = even.next
            odd = even.next
  
            # If there are NO more even nodes  
            # after current odd.  
            if (odd.next == None):  
                even.next = None
                odd.next = evenFirst  
                break
  
            # Connecting even nodes  
            even.next = odd.next
            even = odd.next
        return head 
  
    # A utility function to print a linked list  
    def printlist(self, node):  
        while (node != None):  
            print(node.data, end = "") 
            print("->", end = "") 
            node = node.next
        print ("NULL") 
          
    # Function to insert a new node  
    # at the beginning  
    def push(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node 
  
# Driver code  
ll = LinkedList() 
ll.push(5) 
ll.push(4) 
ll.push(3) 
ll.push(2) 
ll.push(1) 
print ("Given Linked List") 
ll.printlist(ll.head)  
  
start = ll.rearrangeEvenOdd(ll.head)  
  
print ("\nModified Linked List") 
ll.printlist(start) 

