# Radix Sort in Python
# It is also known as Bucket sort.
print()

def Radix_Sort(arr):
    pass




n=int(input('Enter the size of array:  '))
arr=[]
print('\nEnter the Elements')
for i in range(n):
    arr.append(int(input(f'Enter the Element {i+1}: ')))

print('\nElement Before Sorting')
for ele in arr:
    print(ele,end=' ')
max_ele=max(arr)
len_max_ele=len(str(max_ele))

