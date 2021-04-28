# Implementing Queue using two stacks.
print()

class Que_using_stack():
    def __init__(self):
        self.size=int(input("Enter the size of queue: "))
        self.s1=list()
        self.s2=list()

    def Enqueue(self,item):
        if len(self.s1)==self.size:
            print("\nQueue is Full")
        else:
            self.s1.append(item)

    def Dequeu(self):
        if len(self.s1)==0 and len(self.s2)==0:
            print("\nQueue is Empty")
        elif len(self.s2)==0:
            i=len(self.s1)-1
            while i>=0:
                self.s2.append(self.s1[i])
                self.s1.pop()
                i-=1
            self.s2.pop()
        else:
            self.s2.pop()

    def Display(self):
        if len(self.s1)==0 and len(self.s2)==0:
            print("\nQueue is Empty")
        elif len(self.s2)==0:
            for item in self.s1:
                print(item,end=" ")
        elif len(self.s2)!=0 and len(self.s1)!=0:
            for i in range(len(self.s2)):
                print(self.s2[-(i+1)],end=" ")
            for j in range(len(self.s1)):
                print(self.s1[j],end=" ")
        else:
            for k in range(len(self.s2)):
                print(self.s2[-(k+1)],end=" ")

if __name__ == "__main__":
    q=Que_using_stack()

    while True:
        print("\n==============")
        print("1: Enqueue")
        print('2: Dequeue')
        print("3: Display")
        print('4: Exit')
        n=int(input("Enter the choice: "))
        if n==1:
            q.Enqueue(int(input("Enter the Element:  ")))
        elif n==2:
            q.Dequeu()
        elif n==3:
            q.Display()
        elif n==4:
            quit()
        else:
            print("\nInvalid Choice")