# Binary Search Recursive Method.
print()

def Binary_Search(arr,x,low,high):
    if low<=high:

        mid=(low+high)//2
        if x==arr[mid]:
            return mid
        elif x<arr[mid]:
            return Binary_Search(arr,x,low,mid-1)
        else:
            return Binary_Search(arr,x,mid+1,high)
        
    return -1



arr=[]
n=int(input('\nEnter the size of array: '))
print('\nEnter the Element in the Array')
for i in range(n):
    arr.append(int(input(f'Enter Element {i+1}: ')))

x=int(input('\nEnter the Element to Search:  '))

print('\nIndex\tElements')
for z,y in enumerate(arr):
    print(z,'\t',y)

low=0
high=len(arr)-1

result=Binary_Search(arr,x,low,high)

if result>=0:
    print(f'\n{x} found at index {result}')
else:
    print(f'\n{x} not found ')