# Implementing Queue using Linked list.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkd_list():
    def __init__(self):
        self.start=None

    def Insert_at_end(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            x=self.start
            while x.next!=None:
                x=x.next
            x.next=temp

    def Delete_First(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            t=self.start
            t=self.start.next
            self.start=t
    
    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            ptr=self.start
            while ptr!=None:
                print(ptr.data,end='->')
                ptr=ptr.next


if __name__ == "__main__":
    ll=Linkd_list()
    while True:
        print()
        print('=============')
        print('1: Enqueue')
        print('2: Dequeue')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter the Choice: "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insert_at_end(item)
        elif ch==2:
            ll.Delete_First()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')