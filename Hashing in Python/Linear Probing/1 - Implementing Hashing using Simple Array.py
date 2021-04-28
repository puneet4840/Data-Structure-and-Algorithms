# Implementing Hashing using simple array using Linear Probing method.
print()

class Hashing:
    def __init__(self,size):
        self.size=size
        self.hash_table=[None]*self.size

    def Hash_Function(self,key):
        return key%self.size

    def Insert_Ele(self,item):
        index=self.Hash_Function(item)
        i=index
        if self.hash_table[index]==None:
            self.hash_table[index]=item
        else:
            while self.hash_table[i]!=None:
                i+=1
                if i==self.size:
                    i=0
            self.hash_table[i]=item

    def Delete_Ele(self,item):
        flag=0
        index=self.Hash_Function(item)
        if self.hash_table[index]==item:
            self.hash_table[index]=None
            flag=1
        else:
            for i in range(self.size):
                if self.hash_table[i]==item:
                    self.hash_table[i]=None
                    flag=1
                    break
        return flag

    def Search_Ele(self,item):
        flag=0
        i=0
        index=self.Hash_Function(item)
        if self.hash_table[index]==item:
            flag=1
        else:
            while i<self.size:
                if self.hash_table[i]==None:
                    flag=0
                elif self.hash_table[i]==item:
                    flag=1
                    break
                else:
                    flag=0
                i+=1
        return flag

    def Display_Hash_Table(self):
        print('Index \t Data Items')
        for i in range(self.size):
            print(i,': \t',self.hash_table[i])


if __name__=="__main__":
    n=int(input('Enter the size of Hash Table:  '))
    H=Hashing(n)
    while True:
        print('\n==============')
        print('1: Insert Data')
        print('2: Delete Data')
        print('3: Search Data')
        print('4: Display Hash Table')
        print('5: Exit')

        ch=int(input('Enter Your Choice:  '))
        if ch==1:
            ele=int(input('Enter the Element:  '))
            H.Insert_Ele(ele)
        elif ch==2:
            ele=int(input('Enter the Element:  '))
            x=H.Delete_Ele(ele)
            if x==1:
                print('\nElement Deleted.')
            else:
                print('\nElement not found.')
        elif ch==3:
            ele=int(input('Enter the Element to Search: '))
            y=H.Search_Ele(ele)
            if y:
                print('\nElement Present in Hash Table.')
            else:
                print('\nElement not Present.')
        elif ch==4:
            H.Display_Hash_Table()
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')