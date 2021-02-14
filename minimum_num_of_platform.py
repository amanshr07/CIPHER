
# coding: utf-8

# In[1]:


# Function to find the minimum number of platforms needed
# to avoid delay in any train arrival
def minPlatforms(arrival, departure):
 
    # sort arrival time of trains
    arrival.sort()
 
    # sort departure time of trains
    departure.sort()
 
    # maintains the count of trains
    count = 0
 
    # stores minimum platforms needed
    platforms = 0
 
    # take two indices for arrival and departure time
    i = j = 0
 
    # run till all trains have arrived
    while i < len(arrival):
 
        # if a train is scheduled to arrive next
        if arrival[i] < departure[j]:
 
            # increase the count of trains and update minimum
            # platforms if required
            count = count + 1
            platforms = max(platforms, count)
 
            # move the pointer to the next arrival
            i = i + 1
 
        # if the train is scheduled to depart next i.e.
        # `departure[j] < arrival[i]`, decrease trains' count
        # and move pointer `j` to the next departure.
 
        # If two trains are arriving and departing simultaneously, i.e.
        # `arrival[i] == departure[j]`, depart the train first
        else:
            count = count - 1
            j = j + 1
 
    return platforms
 
 
if __name__ == '__main__':
 
    arrival = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
    departure = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
 
    print("The minimum platforms needed is", minPlatforms(arrival, departure))

