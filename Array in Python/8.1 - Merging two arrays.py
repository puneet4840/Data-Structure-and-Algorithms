# Merging means to add two arrays together.
print()

import numpy as np

a1=np.array([1,2,3,4,5])
print(f"Array 1:   {a1}")
a2=np.array([10,20,30,40,50])
print(f"Array 2:   {a2}")

print()

a3=np.concatenate([a1,a2])

print(f"Merged Array:    {a3}")
