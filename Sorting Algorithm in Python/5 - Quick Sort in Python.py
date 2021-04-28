# Quick Sort in Python
print()

def Quick_Sort(arr,low,high):
    if low<high:
        pos=Partioning(arr,low,high)
        Quick_Sort(arr,low,pos-1)
        Quick_Sort(arr,pos+1,high)


def Partioning(arr,low,high):
    pivot_index=low
    pivot=arr[low]
    i=low+1
    j=high

    while i<j:
        while i<len(arr) and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[j],arr[pivot_index]=arr[pivot_index],arr[j]
    return j


n=int(input('Enter the size of array: '))
arr=[]
print('\nEnter the Elements')
for i in range(n):
    arr.append(int(input(f'Enter Element {i+1}: ')))

print('\nElements Before Sorting')
for item in arr:
    print(item,end=' ')

low=0
high=len(arr)-1

Quick_Sort(arr,low,high)

print('\nElements After Sorting')
for item in arr:
    print(item,end=' ')