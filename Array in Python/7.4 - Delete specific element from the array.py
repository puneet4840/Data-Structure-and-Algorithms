# Delete specific element from the array using numpy delete method.
# we first need the require element and its index then we have to give the indx to delete function.
print()

import numpy as np

a=np.random.randint(1,50,10)
print(a)

## Deleting specific element.

# ele=int(input("Enter the element you want to delete:  "))
# if ele in a:
#     for index,item in enumerate(a):
#         if item==ele:
#             new_arr=np.delete(a,index)
#             print("Deleted Array\n")
#             print(new_arr)
# else:
#     print("Element not found")

n=np.delete(a,-1)
print(n)