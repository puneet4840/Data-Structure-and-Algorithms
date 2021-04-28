# Reversing the Linked List using the iterative method.
print()

class Node():
    def __init__(self,data):
        self.data = data
        self.next=None
        

class Linked_List():
    def __init__(self):
        self.start=None
        
    def Insert_at_End(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            p=self.start
            while p.next!=None:
                p=p.next
            p.next=temp

    def Reverse(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            prev=None
            curr=self.start
            post=None
            while curr!=None:
                post=curr.next
                curr.next=prev
                prev=curr
                curr=post
            self.start=prev
    
    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            x=self.start
            while x!=None:
                print(x.data,end='->')
                x=x.next

if __name__=='__main__':   
    ll=Linked_List()
    print()
    while True:
        print('\n================')
        print('1: Insert at End')
        print('2: Revrse Linked List')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            ll.Insert_at_End(item)
        elif ch==2:
            ll.Reverse()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')
