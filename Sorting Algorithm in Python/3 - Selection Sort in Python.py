# Selection Sort Algorithm in Python.
print()

def Selection_Sort(arr):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]




arr=[]
n=int(input('Enter the size of array: '))
print('\nEnter the Elements in the Array:')

for i in range(n):
    arr.append(int(input(f'Enter Element {i+1}: ')))

print('\nArray Before Selection Sort')

for item in arr:
    print(item,end=' ')

Selection_Sort(arr)

print('\nArray After Selection Sort')

for item in arr:
    print(item,end=' ')

