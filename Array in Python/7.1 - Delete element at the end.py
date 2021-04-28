# Deletion of element from the end of the array.
print()

import numpy as np

a=np.random.randint(1,20,5)
print(a)

print()

print("Original Array")
print(a)

print()

print('Deleted Array')
# d=a[-5:-1]
# print(d)


  ## OR

new_arr=np.delete(a,-1)
print(new_arr)