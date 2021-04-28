# Insert an element in Min Heap.
print()

arr=[]
size=int(input("Enter the size of Heap: "))

def Insert_Ele(ele):
    if len(arr)==size:
        print('\nTree is Full')
    else:
        arr.append(ele)
        i=arr.index(ele)
        while i!=0:
            parent=(i-1)//2
            if arr[i]<arr[parent]:
                arr[parent],arr[i]=arr[i],arr[parent]
                i=parent
            else:
                return
    
def Display():
    if len(arr)==0:
        print('\nTree is Empty')
    else:
        for item in arr:
            print(item,end=' ')

if __name__=='__main__':
    while True:
        print('\n===========')
        print('1: Insert Element: ')
        print('2: Display')
        print('3: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            ele=int(input("Enter the Element: "))
            Insert_Ele(ele)
        elif ch==2:
            Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')