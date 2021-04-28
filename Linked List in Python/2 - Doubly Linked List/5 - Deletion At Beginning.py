# Delete the beginning node in linked list.
print()

class Node():
    def __init__(self,data):
        self.prev=None
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
            x=self.start
            while x.next!=None:
                x=x.next
            x.next=temp
            temp.prev=x

    def Delete_Beginning(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            self.start=self.start.next

    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            x=self.start
            while x!=None:
                print(x.data,end='->')
                x=x.next

if __name__ == "__main__":
    LL=Linked_List()
    print()
    while True:
        print('\n============')
        print('1: Insert Node')
        print('2: Delete First Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            LL.Insert_Node(item)
        elif ch==2:
            LL.Delete_Beginning()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid choice')