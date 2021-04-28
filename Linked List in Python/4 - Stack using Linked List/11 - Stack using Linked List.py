# Implementing the stack using the Linked List.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None

    def Insert_node_last(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp

    def Delete_Last(self):
        if self.start==None:
            print('\nLinked list')
        elif self.start.next==None:
            self.start=None
        else:
            x=self.start
            while x.next.next!=None:
                x=x.next
            x.next=None

    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            p=self.start
            while p!=None:
                print(p.data,end="->")
                p=p.next


if __name__=="__main__":
    ll=Linked_list()
    while True:
        print()
        print("==============")
        print('1: Push')
        print('2: Pop')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Yout choice: "))
        
        if ch==1:
            item=int(input("Enter the Element: "))
            ll.Insert_node_last(item)
        elif ch==2:
            ll.Delete_Last()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')
