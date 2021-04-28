# enumerate function is used to return the index as well as its element on the index together.
print()

import numpy as np

arr=np.random.randint(1,200,10)
print(arr)
print()

## Using 'in' operator.

ele=int(input("Enter the element you want to search for:  "))

for index,item in enumerate(arr):
    if item==ele:
        print(f'Element found at index {index}')
        break
    elif ele not in arr:
        print("Element not found")
        break
    
        