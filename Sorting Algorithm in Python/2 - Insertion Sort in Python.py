# Insertion Sort Algorithm in Python.
print()

def Insertion_Sort(arr):
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while temp<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp



arr=[]
n=int(input('Enter the size of Array: '))

print('\nEnter the Elements in Array: ')
for i in range(n):
    arr.append(int(input(f'Enter Element {i+1}: ')))

print('\nElements Before Sorting: ')
for item in arr:
    print(item,end=' ')

Insertion_Sort(arr)

print('\nElements After Sorting: ')
for item in arr:
    print(item,end=' ')