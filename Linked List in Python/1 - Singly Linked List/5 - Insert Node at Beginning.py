# INsert Node at Beginning.
print()


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

    
class Linked_list():
    def __init__(self):
        self.start=None

    def Insert_at_Beg(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            ptr=self.start
            temp.next=ptr
            ptr=temp
            self.start=ptr

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
        print('==================')
        print('1: Insert At The Beginning')
        print('2: Display')
        print('3: Exit')
        ch=int(input("Enter your choice:  "))
        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insert_at_Beg(item)
        elif ch==2:
            ll.Display()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Chocie')
            