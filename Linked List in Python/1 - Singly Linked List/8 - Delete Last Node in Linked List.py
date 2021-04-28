# Deleting Last node in the particular node.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None

    def Insert_Last(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            x=self.start
            while x.next!=None:
                x=x.next
            x.next=temp
        
    def Delete_Last_Node(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            y=self.start
            pre_y=self.start
            if self.start.next==None:
                self.start=None
            else:
                while y.next.next!=None:
                    y=y.next
                y.next=None

    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            ptr=self.start
            while ptr!=None:
                print(ptr.data,end="->")
                ptr=ptr.next

if __name__=="__main__":
    ll=Linked_list()
    while True:
        print()
        print("================")
        print('1: Insert Node in End')
        print('2: Delete Last Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your choice:  "))
        if ch==1:
            item=int(input("Enter the Element: "))
            ll.Insert_Last(item)
        elif ch==2:
            ll.Delete_Last_Node()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')
