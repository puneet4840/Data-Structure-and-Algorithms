# All operation in Stack.
# Push,Pop,Peek(Topmost element),Display.
print()

class Stack():
    def __init__(self):
        self.stk=list()
        self.size=int(input("Enter the size of stack:  "))

    def Push(self):
        if len(self.stk)==self.size:
            print("\n>>> Stack is Full\n")
        else:
            item=int(input("\nEnter the data to store: "))
            self.stk.append(item)
        
    def Pop(self):
        if len(self.stk)==0:
            print("\n>>> Stack is Empty\n")
        else:
            self.stk.pop(-1)

    def Peek(self):
        if len(self.stk)==0:
            print("\n>>> Stack is Empty\n")
        else:
            print(f"\n>>> Topmost element:  {self.stk[-1]}")

    def Display(self):
        if len(self.stk)==0:
            print("\n>>> Stack is Empty\n")
        else:
            print("\n>>> Stack:")
            for ele in self.stk:
                print(ele,end=" ")
            print()

if __name__ == "__main__":
    s=Stack()

    while True:
        print('\n1: Push the element')
        print('\n2: Pop the element')
        print('\n3: Peek the topmost element')
        print('\n4: Display')
        print('\n5: Exit')
        print('\n Enter your choice:   ')
        ch=int(input(" "))

        if ch==1:
            s.Push()
        elif ch==2:
            s.Pop()
        elif ch==3:
            s.Peek()
        elif ch==4:
            s.Display()
        elif ch==5:
            quit()
        else:
            print("\nInvalid Input\n")