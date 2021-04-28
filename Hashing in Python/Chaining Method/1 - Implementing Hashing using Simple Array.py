# Implementing Hashing using simple array and Chaining Technique.
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Hashing:
    def __init__(self,size):
        self.size=size
        self.hash_table=[None]*self.size

    def Hash_Function(self,item):
        return item%self.size

    def Insert_Ele(self,ele1):
        index=self.Hash_Function(ele1)
        start=self.hash_table[index]
        temp=Node(ele1)
        if start==None:
            self.hash_table[index]=temp
        else:
            ptr=start
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=temp


    def Delete_Ele(self,ele2):
        index=self.Hash_Function(ele2)
        start=self.hash_table[index]
        if start==None:
            print('\nElement Not Present')
        else:
            ptr=start
            prev=ptr
            while ptr!=None and ptr.data!=ele2:
                prev=ptr
                ptr=ptr.next
            if ptr.next==None:
                prev.next=None
            elif prev==ptr:
                self.hash_table[index]=ptr.next
            else:
                prev.next=ptr.next


    def Search_Ele(self,ele3):
        index=self.Hash_Function(ele3)
        start=self.hash_table[index]
        ptr=start
        while ptr.data!=ele3 and ptr!=None:
            ptr=ptr.next
        if ptr==None:
            print('\nElement Not Present in Hash Table')
        else:
            return ptr.data

    def Display_Hash_Table(self):
        print('\nIndex    Data Items')
        for i in range(self.size):
            start=self.hash_table[i]
            ptr=start
            if self.hash_table[i]==None:
                print(i,':\t',self.hash_table[i])
            else:
                print(i,end=':\t')
                while ptr!=None:
                    print(ptr.data,end='-> ')
                    ptr=ptr.next
                print()

if __name__=="__main__":
    n=int(input('Enter the size of Hash Table:  '))
    H=Hashing(n)
    while True:
        print('\n=================')
        print('1: Insert Data ')
        print('2: Delete Data ')
        print('3: Search Data ')
        print('4: Display Hash Table')
        print('5: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item_Insert=int(input('Enter the Element: '))
            H.Insert_Ele(item_Insert)
        
        elif ch==2:
            item_Delete=int(input('Enter the Element:  '))
            H.Delete_Ele(item_Delete)
        
        elif ch==3:
            item_Search=int(input('Enter the Element:  '))
            data=H.Search_Ele(item_Search)
            print(f'\n{data} is present in the Hash Table')
        
        elif ch==4:
            H.Display_Hash_Table()
        
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')