# Insert node before a given node.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

    
class Linked_list():
    def __init__(self):
        self.start=None

    def Create_list(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp

    def Insert_before_given(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            ele=int(input("Enter the Element in New Node: "))
            new_node=Node(ele)
            node_ele=int(input("Enter the Data, Before to insert node:  "))
            x=self.start
            pre_ptr=self.start
            if node_ele==self.start.data:
                temp=self.start
                temp=new_node
                new_node.next=self.start
                self.start=temp
            else:
                while x.next!=None:
                    x=x.next
                    if x.data==node_ele:
                        pre_ptr.next=new_node
                        new_node.next=x
                        break
                    pre_ptr=pre_ptr.next

    def Display(self):
        if self.start==None:
            print("\nLinked LIst is Empty")
        else:
            y=self.start
            while y!=None:
                print(y.data,end="->")
                y=y.next

if __name__=="__main__":
    ll=Linked_list()
    while True:
        print()
        print("================")
        print('1: Create Linked List')
        print('2: Insert Node Before a Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your Choice:  "))
        if ch==1:
            item=int(input("Enter the ELement: "))
            ll.Create_list(item)
        elif ch==2:
            ll.Insert_before_given()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print("\nInvalid Choice")