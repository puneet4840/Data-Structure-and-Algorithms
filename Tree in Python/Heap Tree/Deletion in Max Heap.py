# Deletion in Max Heap.
print()

arr=[]
size=int(input("Enter the size of Tree:  "))

def Insert_Element(ele):
    if len(arr)==size:
        print('\nTree is Full')
    else:
        arr.append(ele)
        i=arr.index(ele)
        while i!=0:
            parent=(i-1)//2
            if arr[parent]<arr[i]:
                arr[parent],arr[i]=arr[i],arr[parent]
                i=parent
            else:
                return
        
def Delete_Element():
    if len(arr)==0:
        print('\nTree is Empty')
    else:
        first=arr[0]
        last=arr[-1]
        arr[0],arr[-1]=arr[-1],arr[0]
        arr.pop(-1)
        down_heapify(arr,0,len(arr))

def down_heapify(arr,parent,size):
    largest=parent
    l_c=(2*parent)+1
    r_c=(2*parent)+2
    if l_c<size and arr[l_c]>arr[largest]:
        largest=l_c
    if r_c<size and arr[r_c]>arr[largest]:
        largest=r_c
    if parent!=largest:
        arr[parent],arr[largest]=arr[largest],arr[parent]
        down_heapify(arr,largest,size)

def Display():
    if len(arr)==0:
        print('\nTree is Empty')
    else:
        for item in arr:
            print(item,end=' ')

if __name__=="__main__":
    while True:
        print('\n==========')
        print('1: Insert Node')
        print('2: Delete Element')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            ele=int(input("Enter the Element: "))
            Insert_Element(ele)
        elif ch==2:
            Delete_Element()
        elif ch==3:
            Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')