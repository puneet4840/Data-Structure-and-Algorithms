# Delete first node of the circular linked list.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_List():
    def __init__(self):
        self.last=None

    def Insert_end(self,data):
        temp=Node(data)
        if self.last==None:
            self.last=temp
            self.last.next=self.last
        else:
            temp.next=self.last.next
            self.last.next=temp
            self.last=temp

    def Delete_beg(self):
        if self.last==None:
            print('\nLinked List is Empty')
        else:
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
        
    def Display(self):
        if self.last==None:
            print('\nLinked List is Empty')
        else:
            p=self.last.next
            while True:
                print(p.data,end='->')
                p=p.next
                if p==self.last.next:
                    break

if __name__=="__main__":
    LL=Linked_List()
    print()
    while True:
        print('\n===========')
        print('1: Insert Node')
        print('2: Delete First Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            LL.Insert_end(item)
        elif ch==2:
            LL.Delete_beg()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')