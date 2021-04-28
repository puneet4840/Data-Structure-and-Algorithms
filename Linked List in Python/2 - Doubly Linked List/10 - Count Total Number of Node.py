# Count Total Numer Of Nodes in Doubly Linked List.
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

    def Count_Nodes(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            count=1
            if self.start.next==None:
                print(f'\n{count} Node Present in the Linked List')
            else:
                ptr=self.start
                while ptr.next!=None:
                    ptr=ptr.next
                    count+=1
                if count==0:
                    print('\nLinked List is Empty')
                else:
                    print(f'{count} nodes present in the Linked List')

    def Display(self):
        if self.start==None:
            print('\nLinked list is Empty')
        else:
            x=self.start
            while x!=None:
                print(x.data,end='->')
                x=x.next

if __name__ == "__main__":
    LL=Linked_list()
    print()
    while True:
        print('\n=============')
        print('1: Insert Node')
        print('2: Count Nodes')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter Your Choice:  "))
            LL.Insert_Node(item)
        elif ch==2:
            LL.Count_Nodes()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')