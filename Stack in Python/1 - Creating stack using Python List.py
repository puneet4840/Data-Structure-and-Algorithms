# Stack is the collection of elements in a ordered way.
# Insertion in stack is done on top of the stack.
# Deletion in stack is done on top of the stack.
# If follows LIFO rule
## LIFO (Last In First Out).
print()

class Stack():
    def __init__(self):
        self.stk=[]
        self.size=int(input("Enter the size of stack:  "))

    def push(self):
        if len(self.stk)==self.size:
            print("\nStack is Full\n")
        else:
            item=int(input("Enter the element to insert in the stack:  "))
            self.stk.append(item)
    
    def pop(self):
        if len(self.stk)==0:
            print('\nStack is Empty\n')
        else:
            self.stk.pop(-1)
    
    def display(self):
        if len(self.stk)==0:
            print("\nStack is Empty\n")
        else:
            print("\n")
            print("Stack: ")
            for ele in self.stk:
                print(ele,end=" ")



if __name__ == "__main__":
    s=Stack()
    while True:
        print("\n\n 1: Push the element")    
        print("\n 2: Pop the element")
        print("\n 3: Display the Stack")
        print("\n 4: Exit")
        print("\n Enter your choice: ")
        n=int(input(" "))

        if n==1:
            s.push()
            # break
        elif n==2:
            s.pop()
            # break
        elif n==3:
            s.display()
            # break
        elif n==4:
            quit()
