# Insertion at the end in the Circular Linked List.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_List():
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

    def Display(self):
        if self.last==None:
            print('\nLinked List is Empty')
        else:
            p=self.last.next
            while True:
                print(p.data,end="->")
                p=p.next
                if p==self.last.next:
                    break

if __name__ == "__main__":
    LL=Linked_List()
    print()
    while True:
        print('\n============')
        print('1: Insert Node at End')
        print('2: Display')
        print('3: Exit')
        ch=int(input("Enter your choice:  "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            LL.Insert_End(item)
        elif ch==2:
            LL.Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')