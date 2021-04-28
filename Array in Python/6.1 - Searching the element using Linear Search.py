# We are about to search the element in the array.
print()

import numpy as np

a=np.random.randint(1,100,5)
print("Original Array\n")
print(a)
print()

## Searching the element in the array using module

ele=int(input("Enter the element to search in array: "))
i=0
flag=True

while i<len(a):
    if a[i]==ele:
        flag=False
        break
    else:
        i+=1
if flag==False:
    print(f"Element found at position: {i}")
elif flag==True:
    print("Element not found")