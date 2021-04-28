# Insert node at the End.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


class Linked_list():
    def __init__(self):
        self.start=None

    def Insert_AT_End(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp
        
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
        print("===============")
        print('1: Insert at End')
        print('2: Display')
        print('3: Exit')
        ch=int(input("Enter your choice:  "))
        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insert_AT_End(item)
        elif ch==2:
            ll.Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')