# Deletion of Entire List.
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class Linked_list():
    def __init__(self):
        self.start=None
        
    def Insert_Node(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            p=self.start
            while p.next!=None:
                p=p.next
            p.next=temp
            temp.prev=p
            
    def Delete_Entire_List(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            self.start=None
            print("\nLinked List Deleted")

    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            q=self.start
            while q!=None:
                print(q.data,end='->')
                q=q.next

if __name__ == "__main__":
    LL=Linked_list()
    print()
    while True:
        print('\n============')
        print('1: Insert Node')
        print('2: Delete Entire List')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            LL.Insert_Node(item)
        elif ch==2:
            LL.Delete_Entire_List()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')