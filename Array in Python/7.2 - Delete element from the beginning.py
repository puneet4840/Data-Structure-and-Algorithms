# Deleting the element from the beginning of the array.
# We can go tot the approach like we can create the view of the array using string indexing like [:-1]
print()

import numpy as np

a=np.random.randint(1,50,5)
print(a)

## Deleting the element from the beginning of the array.

print("Original Array\n")
print(a)

print()

## View of the array.

# d=a[1:]

print("Deleted Array\n")
# print(d)
  
  ## OR

new_arr=np.delete(a,0)
print(new_arr)