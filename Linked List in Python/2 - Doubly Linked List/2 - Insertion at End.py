# Insert the node at the end of linked list.
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class Linked_list():
    def __init__(self):
        self.start=None
        
    def Insert_at_end(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp
            temp.prev=ptr
    
    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            x=self.start
            while x!=None:
                print(x.data,end='->')
                x=x.next
    
if __name__=="__main__":
    LL=Linked_list()
    print()
    while True:
        print('\n=============')
        print('1: Insert Node at End')
        print('2: Display')
        print('3: Exit')
        ch=int(input("Enter your choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            LL.Insert_at_end(item)
        elif ch==2:
            LL.Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')