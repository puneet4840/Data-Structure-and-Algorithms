# Linear search in python.
print()

def Linear_Search(x,n,lst):
    flag=0
    for i in range(n):
        if lst[i]==x:
            flag=1
            break
        else:
            flag=0

    if flag:
        print(f'\n{x} Found at index: {i}')
    else:
        print('\nElement not Found')


lst=[]
n=int(input('Enter the size of array:  '))
print('\nEnter the Elments in the array: ')
for i in range(n):
    lst.append(int(input(f'Enter Element {i+1}: ')))

x=int(input('Enter the Element to Search: '))

print('\nElements Are:')
print('Index\tElement')
for z,j in enumerate(lst):
    print(z,'\t',j)

Linear_Search(x,n,lst)