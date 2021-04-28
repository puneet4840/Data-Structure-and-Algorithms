# Ciurcular singly linked list.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List():
    def __init__(self):
        self.last=None
    
    def Insert_Beginning(self,data):
        temp=Node(data)
        if self.last==None:
            self.last=temp
            self.last.next=self.last
        else:
            p=self.last
            temp.next=self.last.next
            self.last.next=temp
    
    def Display(self):
        if self.last==None:
            print("\nLinked List is Empty")
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
        print('\n=============')
        print('1: Insert Node at Beginning')
        print('2: Display')
        print('3: Exit')
        ch=int(input("Enter your choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            LL.Insert_Beginning(item)
        elif ch==2:
            LL.Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')