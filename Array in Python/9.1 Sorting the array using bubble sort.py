# Here i am using the sorting of array using bubble sort.
print()

import numpy as np

a=np.random.randint(1,100,5)
print(f"Unsorted Array:    {a}")

## Bubble sort

print()

print("Sorted Array\n")

def Bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
        print(f" Pass i {i+1}:   {a}")

Bubble_sort(a)
print('\n',a)
