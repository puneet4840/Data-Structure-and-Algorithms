# Matrix in Python.
print()

import numpy as np


# 2*2 matrix.
print('Matix 1 (2*2)')
m1=np.eye(2,2)
print(m1)
print()


# 3*3 matrix
print('Matrix 2 (3*3)')
m2=np.diag([1,2,3])
print(m2)
print()

# 5*5 matrix
print('Matrix 3 (5*5)')
m3=np.arange(1,26).reshape(5,-1)
print(m3)
print()
             #OR
            
print('Randon numbers Matrix 4 (5*5)')
m4=np.random.randint(1,50,25).reshape(-1,5)
print(m4)