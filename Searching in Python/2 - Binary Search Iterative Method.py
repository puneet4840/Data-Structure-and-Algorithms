# Binary Search (Iterative Method).
print()

def Binary_Search(x,n,lst,low,high):
    while low<=high:
        mid=(low+high)//2
        if x==lst[mid]:
            return mid
        elif x<lst[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1



lst=[]
n=int(input('Enter the size of Array:  '))
print('\nEnter the Elements in Array (In Sorted Order)')
for i in range(n):
    lst.append(int(input(f'Enter the Element {i+1}: ')))

x=int(input('\nEnter the Element to Search: '))
print('\nElement are:')
print('\nIndex\tElement')
for z,y in enumerate(lst):
    print(z,'\t',y)
low=0
high=len(lst)-1

result=Binary_Search(x,n,lst,low,high)
if result>=0:
    print(f'\nElement found at index {result}')
else:
    print(f'\nElement not found')