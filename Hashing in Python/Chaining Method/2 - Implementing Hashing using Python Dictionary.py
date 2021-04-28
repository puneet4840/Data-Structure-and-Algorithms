# Implementing Hashing using Python Dictionary.
print()

class Hashing:
    def __init__(self,size):
        self.size=size
        self.hash_table=dict()

        for i in range(self.size):
            self.hash_table[i]=[]

    def Hash_Function(self,key):
        return key%self.size

    def Insert_Ele(self,item):
        index=self.Hash_Function(item)
        self.hash_table[index].append(item)

    def Delete_Ele(self,item):
        index=self.Hash_Function(item)
        if item not in self.hash_table[index]:
            print('\nElement not present in Hash Table')
        else:
            i1=self.hash_table[index].index(item)
            self.hash_table[index].pop(i1)

    def Search_Ele(self,item):
        index=self.Hash_Function(item)
        if item in self.hash_table[index]:
            print('\nElement Present in Hash Table')
        else:
            print('\nElement Not Present in Hash Table')

    def Display_Hash_Table(self):
        print('\nIndex \tData Items')
        for i in range(self.size):
            print(i,end=": ")
            if len(self.hash_table[i])==0:
                print('None')
            else:
                for item in self.hash_table[i]:
                    print(item,end='->')
            print()

    
if __name__=="__main__":
    n=int(input('Enter the Size of Hash Table: '))
    H=Hashing(n)
    while True:
        print('\n==============')
        print('1: Insert Data')
        print('2: Delete Data')
        print('3: Search Element')
        print('4: Display Hash Table')
        print('5: Exit')
        ch=int(input('Enter Your Choice:  '))

        if ch==1:
            ele=int(input('Enter the Insert Element:  '))
            H.Insert_Ele(ele)

        elif ch==2:
            ele=int(input('Enter the Delete Element:  '))
            H.Delete_Ele(ele)
        
        elif ch==3:
            ele=int(input('Enter the Search Element:  '))
            H.Search_Ele(ele)

        elif ch==4:
            H.Display_Hash_Table()

        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')