# Reverse a string using stack.
# We first push the string into stack and pop the string from the stack.
# Hence, string would be reversed.
print()

class Stack():
    def __init__(self):
        self.stk=list()
        self.str=input("Enter a string:  ")

    def Push(self):
        for chr in self.str:
            self.stk.append(chr)
        
    def Pop(self):
        print("\nReversed String:")
        i=len(self.stk)-1
        while i>=0:
            print(self.stk[i],end="")
            i-=1

if __name__ == "__main__":
    s=Stack()
    s.Push()
    s.Pop()
