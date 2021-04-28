# Heap Sort in Python.
print()

def Heap_Sort(max_heap):
    result_arr=[]
    while len(max_heap)!=0:
        result_arr.insert(0,max_heap[0])
        max_heap[0],max_heap[-1]=max_heap[-1],max_heap[0]
        max_heap.pop(-1)
        Heapify(max_heap,0,len(max_heap))
    return result_arr

def Heapify(max_heap,parent,size):
    largest=parent
    l_child=(2*parent)+1
    r_child=(2*parent)+2
    
    if l_child<size and max_heap[l_child]>max_heap[largest]:
        largest=l_child
    if r_child<size and max_heap[r_child]>max_heap[largest]:
        largest=r_child
    if parent!=largest:
        max_heap[parent],max_heap[largest]=max_heap[largest],max_heap[parent]
        Heapify(max_heap,largest,size)




def Build_Max_Heap(arr,max_heap):
    for k in range(len(arr)):
        max_heap.append(arr[k])
        ind=max_heap.index(arr[k])
        while ind>0:
            parent=(ind-1)//2
            if max_heap[parent]<max_heap[ind]:
                max_heap[parent],max_heap[ind]=max_heap[ind],max_heap[parent]
                ind=parent
            else:
                break


if __name__=="__main__":
    arr=[]
    max_heap=[]
    n=int(input('Enter the size of array: '))
    print('\nEnter the Elements')
    for i in range(n):
        arr.append(int(input(f"Enter Element {i+1}: ")))

    print('\nElements Before Sorting')
    for j in range(n):
        print(arr[j],end=' ')

    Build_Max_Heap(arr,max_heap)
    re=Heap_Sort(max_heap)
    print('\nElement After Heap Sort')
    for item in re:
        print(item,end=' ')

