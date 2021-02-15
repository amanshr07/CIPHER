
# coding: utf-8

# In[10]:


def toString(List):
   return ''.join(List)
# permutations
def permute(a, l, r):
   if l == r:
      print (toString(a))
   else:
      for i in range(l, r + 1):
         a[l], a[i] = a[i], a[l]
         permute(a, l + 1, r)
         a[l], a[i] = a[i], a[l] # backtracking
# main
string = "TUT"
n = len(string)
a = list(string)
print("The possible permutations are:",end="\n")
permute(a, 0, n-1)

