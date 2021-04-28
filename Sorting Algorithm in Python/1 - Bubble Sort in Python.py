# Bubble Sort in Python.
print()

def Bubble_Sort(arr):
    for i in range(1,n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]




n=int(input('Enter the size of array:  '))
arr=[]
print('\nEnter the Elements')

for i in range(n):
    arr.append(int(input(f'Enter the Element {i+1}: ')))

print('\nElements Before Bubble Sorting:')

for item in arr:
    print(item,end=' ')

Bubble_Sort(arr)

print('\nElements After Bubble Sorting:')

for item in arr:
    print(item,end=' ')
print()