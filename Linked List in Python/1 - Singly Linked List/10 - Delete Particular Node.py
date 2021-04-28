# Delete Psrticular node.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None

    def Insert_end(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp

        else:
            x=self.start
            while x.next!=None:
                x=x.next
            x.next=temp
        
    def Delet_particular(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            ele=int(input("Enter the Data of node which you want to delete: "))
            ptr=self.start
            pre_ptr=self.start
            if ele==self.start.data:
                self.start=self.start.next
            elif self.start.next==None:
                self.start=None
            else:
                while ptr.data!=ele:
                    pre_ptr=ptr
                    ptr=ptr.next
                pre_ptr.next=ptr.next

        

    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            z=self.start
            while z!=None:
                print(z.data,end='->')
                z=z.next


if __name__=='__main__':
    ll=Linked_list()
    while True:
        print()
        print('===============')
        print('1: Insert Element')
        print('2: Delete Particular Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
            item=int(input("Enter the Element:  "))
            ll.Insert_end(item)
        elif ch==2:
            ll.Delet_particular()
        elif ch==3:
            ll.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')
