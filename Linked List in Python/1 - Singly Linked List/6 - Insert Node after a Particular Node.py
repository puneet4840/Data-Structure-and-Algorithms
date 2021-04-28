# Insert node after a particular node in singly linked list.
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
        
    def Insert_after_particular(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            item1=int(input("Enter the Element: "))
            new_node=Node(item1)
            node_data=int(input("Enter the Data of node after which you eant to insert the data: "))
            if node_data==self.start.data:
                x=self.start.next
                self.start.next=new_node
                new_node.next=x
            else:
                p=self.start
                post_p=p.next
                while p.data!=node_data:
                    p=p.next
                    post_p=p.next
                if p.next==None:
                    p.next=new_node
                else:
                    p.next=new_node
                    new_node.next=post_p


    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            ptr=self.start
            while ptr!=None:
                print(ptr.data,end="->")
                ptr=ptr.next

if __name__ == "__main__":

    ll=Linked_list()
    while True:
        print()
        print("====================")
        print('1: Create Linked List')
        print('2: Insert Node after a Particular Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your choice:  "))
        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insert_End(item)
        
        elif ch==2:
            ll.Insert_after_particular()
        
        elif ch==3:
            ll.Display()
        
        elif ch==4:
            quit()
        else:
            print("\nInvalid Chocie")