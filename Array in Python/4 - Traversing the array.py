# Traversing (Visiting) the array.
print()

import numpy as np

### 1-D array
a1=np.array([10,20,30,40,50])
    # without index
for elements in a1:
    print(elements,end=" ")

print()

    # with index
i=0
while i<len(a1):
    print(a1[i],end=" ")
    i+=1

print()

### 2-D array
a2=np.arange(1,5).reshape(2,-1)
    # without index
for item in a2:
    print(item)

print()

    # with index
i=0
while i<len(a2):
    j=0
        print(a2[i][j])
        j+=1
    i+=1