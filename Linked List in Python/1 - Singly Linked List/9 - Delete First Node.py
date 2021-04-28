# Delete First Node
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

    
class Linked_list():
    def __init__(self):
        self.start=None

    def Insert_End(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp
    
    def Delete_First(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            ptr=self.start
            ptr=self.start.next
            self.start.next=None
            self.start=ptr
        
    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            x=self.start
            while x!=None:
                print(x.data,end="->")
                x=x.next

if __name__=="__main__":
    ll=Linked_list()
    while True:
        print()
        print("==================")
        print('1: Insert Node at End')
        print('2: Delete Fisrt Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            ll.Insert_End(item)
        elif ch==2:
            ll.Delete_First()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')