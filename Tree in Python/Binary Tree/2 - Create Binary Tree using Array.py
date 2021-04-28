# Binary Tree (Array Implementation).
print()

import numpy as np

arr=list()

size=int(input("Enter the size of array:  "))

def Insert_Ele(ele):
    if len(arr)==size:
        print('\nTree is Full')
    else:
        arr.append(ele)

def Print_Tree(arr):
    if len(arr)==0:
        print('\nNo nodes in the Tree')
    else:
        for item in arr:
            print(item,end=' ')

def Find_root():
    if len(arr)==0:
        print('\nNo nodes in the Tree')
    else:
        return arr[0]

def find_Parent(pos):
    if len(arr)==0:
        print('\nNo nodes in the Tree')
    else:
        return arr[(pos-1)//2]

def Right_child(pos1):
    if len(arr)==0:
        print('\nNo nodes in the Tree')
    else:
        return arr[(2*pos1)+2]

def Left_child(pos2):
    if len(arr)==0:
        print('\nNo nodes in the Tree')
    else:
        return arr[(2*pos2)+1]

if __name__=="__main__":
    while True:
        print()
        print('\n==============')
        print('1: Insert Element')
        print('2: Display Tree Element')
        print('3: Find Root Node')
        print('4: Find Parent Node')
        print('5: Find Left Child')
        print('6: Find Right Child')
        print('7: Exit')
        ch=int(input("\nEnter Your Choice:  "))

        if ch==1:
            ele=int(input("Enter the Element:  "))
            Insert_Ele(ele)
        elif ch==2:
            Print_Tree(arr)
        elif ch==3:
            a=Find_root()
            print(a)
        elif ch==4:
            pos=int(input("Enter the Position of element: "))
            b=find_Parent(pos)
            print(b)
        elif ch==5:
            pos2=int(input("Enter the Position of element: "))
            c=Left_child(pos2)
            print(c)
        elif ch==6:
            pos1=int(input("Enter the Position of element: "))
            d=Right_child(pos1)
            print(d)
        elif ch==7:
            quit()