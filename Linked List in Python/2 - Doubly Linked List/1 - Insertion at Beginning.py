# Insertion of node at the beginning in the Doubly Linked List.
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None
        
    def Insertion_At_Beginning(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            p=self.start
            p=temp
            p.next=self.start
            self.start.prev=p
            self.start=p
        
    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            x=self.start
            while x!=None:
                print(x.data,end="->")
                x=x.next
    
if __name__=="__main__":
    ll=Linked_list()
    print()
    while True:
        print('\n=============')
        print('1: Insert Node at Beginning')
        print('2: Display Node')
        print('3: Exit')
        ch=int(input("Enter your choice:  "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insertion_At_Beginning(item)
        elif ch==2:
            ll.Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid choice')
            