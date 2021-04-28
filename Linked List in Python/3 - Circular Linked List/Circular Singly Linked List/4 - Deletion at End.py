# Delete the last node in Linked List.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_list():
    def __init__(self):
        self.last=None

    def Insert_End(self,data):
        temp=Node(data)
        if self.last==None:
            self.last=temp
            self.last.next=self.last
        else:
            temp.next=self.last.next
            self.last.next=temp
            self.last=temp
            
    def Delete_at_End(self):
        if self.last==None:
            print("\nLinked List is Empty")
        else:
            p=self.last.next
            q=p.next
            while p.next!=self.last:
                p=p.next
                q=p.next
            if self.last.next==self.last:
                self.last=None
            else:
                self.last=p
                self.last.next=q.next

    def Display(self):
        if self.last==None:
            print('\nLinked List is Empty')
        else:
            x=self.last.next
            while True:
                print(x.data,end='->')
                x=x.next
                if x==self.last.next:
                    break

if __name__=='__main__':
    LL=Linked_list()
    print()
    while True:
        print('\n==========')
        print('1: Insert Node')
        print('2: Delete Last Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your choice: "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            LL.Insert_End(item)
        elif ch==2:
            LL.Delete_at_End()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')
