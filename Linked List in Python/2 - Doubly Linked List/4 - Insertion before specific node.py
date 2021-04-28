# Inserting a node before a specific node in the linked list.
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None

    def insert_node(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            x=self.start
            while x.next!=None:
                x=x.next
            x.next=temp
            temp.prev=x

    def Insert_Node_Before(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            ele=int(input("Enter the Element in new node: "))
            new_node=Node(ele)
            node_data=int(input("Enter the node before insert node:  "))
            if node_data==self.start.data:
                x=new_node
                new_node.next=self.start
                self.start.prev=new_node
                self.start=x
            else:
                ptr=self.start
                pre_ptr=None
                while ptr.data!=node_data:
                    pre_ptr=ptr
                    ptr=ptr.next
                if ptr.next==None:
                    pre_ptr.next=new_node
                    new_node.next=ptr
                    new_node.prev=pre_ptr
                    ptr.prev=new_node
                else:
                    pre_ptr.next=new_node
                    new_node.next=ptr
                    new_node.prev=pre_ptr
                    ptr.prev=new_node
    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            q=self.start
            while q!=None:
                print(q.data,end='->')
                q=q.next
        
if __name__=='__main__':
    LL=Linked_list()
    print()
    while True:
        print()
        print('\n===============')
        print('1: Insert Node in End')
        print('2: Insert Node Before a given Node: ')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter the choice:  "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            LL.insert_node(item)
        elif ch==2:
            LL.Insert_Node_Before()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\n Invalid Choice')