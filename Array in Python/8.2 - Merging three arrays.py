# Merging three arrays.
print()

import numpy as np

a1=np.array((1,2,3,4,5))
a2=np.array((10,20,30,40,50))
a3=np.array((100,200,300,400,500))

print(f"Arrays:  {a1} -> {a2} -> {a3}")

print()

a4=np.concatenate([a1,a2,a3])
print(f"Merged Array:   {a4}")