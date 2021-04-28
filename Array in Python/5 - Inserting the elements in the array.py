# Inserting the element in the end of array.
print()

import numpy as np

## Inserting the element in the end of array using module.
a=np.array([10,20,30,40,50])
print("Inserting at the end\n")
print("Original array")
print(a)
print()
print("Array after insertion")
b1=np.append(a,60)
print(b1)
print()

## Inserting the element in the beginning of the array.
print("Inserting at the beginning\n")
print("Original Array")
print(a)
print()
print("Array after insertion")
b2=np.insert(a,0,1)
print(b2)
print()

## Inserting the element in the array at any position.
print("Insesrting at any position\n")
print("Original Array")
print(a)
print()

pos=int(input("Enter the position to insert the element: "))
print("Array after insertion")
b3=np.insert(a,pos,999)
print(b3)
