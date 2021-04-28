# Merge Sort in Python
print()

def Merge_Sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        Merge_Sort(left)
        Merge_Sort(right)
        Merging(arr,left,right)

def Merging(arr,left,right):
    left_len=len(left)
    right_len=len(right)
    i=j=k=0
    while i<left_len and j<right_len:
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
    while i<left_len:
        arr[k]=left[i]
        i+=1
        k+=1
    while j<right_len:
        arr[k]=right[j]
        j+=1
        k+=1





n=int(input('Enter the size of array: '))
arr=[]
print('\nEnter the Elements: ')

for i in range(n):
    arr.append(int(input(f'Enter Element {i+1}: ')))

print('\nElements Before Sorting')
for item in arr:
    print(item,end=' ')

Merge_Sort(arr)

print('\nElements After Sorting')
for item in arr:
    print(item,end=' ')