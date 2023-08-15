#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Ishanya

import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Generate a random array of numbers
array_size = 20
random_array = [random.randint(1, 1000000) for _ in range(array_size)]

# Sort the array
random_array.sort()

# Print the sorted array
print("Sorted Random Array:", random_array)

# Search for a target value
target = random_array[random.randint(0, array_size - 1)]
result = binary_search(random_array, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")


# In[ ]:




