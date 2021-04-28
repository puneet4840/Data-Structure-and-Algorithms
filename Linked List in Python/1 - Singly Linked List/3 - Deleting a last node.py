# Deleting a last node from linked list.
print()

class Node():
    def __init__(self,data):
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

    def Delete_last_node(self):
        if self.start==None:
            print("\nLinked List is Empty")
        elif self.start.next==None:
            self.start=None
        else:
            ptr1=self.start
            # pre_ptr=self.start
            while ptr1.next.next!=None:
                # pre_ptr=ptr1
                ptr1=ptr1.next
            ptr1.next=None

    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            ptr=self.start
            while ptr!=None:
                print(ptr.data,end="->")
                ptr=ptr.next

if __name__ == "__main__":

    ll=Linked_list()

    while True:
        print()
        print('=======================')
        print("1: Insert node in last")
        print('2: Delete Node at last')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your choice:  "))
        
        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insert_at_end(item)
        elif ch==2:
            ll.Delete_last_node()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')