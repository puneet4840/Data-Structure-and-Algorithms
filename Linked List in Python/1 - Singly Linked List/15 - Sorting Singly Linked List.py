# Bubble sort techniques to sort the singly linked list.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_list():
    def __init__(self):
        self.start=None
        self.count=1
        
    def Insert_Node(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp
            self.count+=1
            
    def Bubble_Sort(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            curr=self.start
            index=None
            temp=None
            while curr!=None:
                index=curr.next
                while index!=None:
                    if curr.data>index.data:
                        temp=curr.data
                        curr.data=index.data
                        index.data=temp
                    index=index.next
                curr=curr.next

    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            x=self.start
            while x!=None:
                print(x.data,end='->')
                x=x.next
            

if __name__ == "__main__":
    LL=Linked_list()
    print()
    while True:
        print('\n============')
        print('1: Insert Node')
        print('2: Sort Linked List')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            LL.Insert_Node(item)
        elif ch==2:
            LL.Bubble_Sort()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')