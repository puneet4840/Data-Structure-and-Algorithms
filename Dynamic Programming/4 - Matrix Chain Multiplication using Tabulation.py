# Matrix Chain Miltiplication using Tabulation Method.
print()

import sys

def Matrix_Chain_Mul(arr,y):
    C=[[0 for i in range(y)] for i in range(y)]
    # C[i][i]==0

    for i in range(y):
        C[i][i]=0

    for L in range(2,y):
        for i in range(1,y-L+1):
            j=i+L-1
            C[i][j]=sys.maxsize
            for k in range(i,j):
                q=C[i][k]+C[k+1][j]+arr[i-1]*arr[k]*arr[j]
                if q<sys.maxsize:
                    C[i][j]=q
    return C[1][y-1]





arr=[]
# n=int(input('Enter the number of Matrices:  '))
x=int(input('Enter the number of Dimenstion of Matrices:  '))
print('\nEnter the Dimension')
for i in range(x):
    arr.append(int(input(f'Enter the Dimension {i+1}:  ')))

result=Matrix_Chain_Mul(arr,len(arr))
print(result)