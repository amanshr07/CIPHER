
# coding: utf-8

# In[7]:


def numberOfPaths(m, n): 
# If either given row number is first 
# or given column number is first 
    if(m == 1 or n == 1): 
        return 1
  
# If diagonal movements are allowed 
# then the last addition 
# is required. 
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 
  
# Driver program to test above function  
m = 3
n = 3
print(numberOfPaths(m, n))

