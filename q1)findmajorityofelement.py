
# coding: utf-8

# In[3]:


def majority(arr,n):
    maxcount=0;
    index=-1
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count > maxcount:
            maxcount=count
            index=i
    if maxcount>n/2:
        print(arr[index])
    else:
        print("no majority element")
arr=[1,1,1,2,4,5,1]
n=len(arr)
majority(arr,n)
    

