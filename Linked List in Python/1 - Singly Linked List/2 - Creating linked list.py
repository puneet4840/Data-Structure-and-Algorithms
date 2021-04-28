# Linked List is the collection of nodes which randomly stores in the memory.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List():
    def __init__(self):
        self.start=None

    def Insert_Node(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp
    
    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            ptr=self.start
            while ptr!=None:
                print(ptr.data,end="-->")
                ptr=ptr.next

    
if __name__ == "__main__":
    ll=Linked_List()
    while True:
        print()
        print('========================')
        print('1: Insert Node at the end')
        print('2: Display Linked List')
        print('3: Exit')
        ch=int(input("Enter your choice: "))
        
        if ch==1:
            item=int(input("Enter the Data: "))
            ll.Insert_Node(item)
        
        elif ch==2:
            ll.Display()

        elif ch==3:
            quit()
        else:
            print("\nInvalid Choice")