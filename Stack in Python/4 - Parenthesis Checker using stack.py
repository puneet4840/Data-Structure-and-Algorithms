# Parenthesis Checker: It returns true when open parenthesis is equal to the closing parenthesis.
print()

class Stack():
    def __init__(self):
        self.stk=list()

    def Push(self,char):
        self.stk.append(char)

    def Pop(self):
        self.stk.pop(-1)


if __name__ == "__main__":
    s=Stack()


    def compare(opening,closing):
        if opening=="(" and closing==")":
            return True
        elif opening=="{" and closing=="}":
            return True
        elif opening=="[" and closing=="]":
            return True
        else:
            return False

    st=input("Enter expression:  ")
    
    for item in st:
        if item=="(" or item=="{" or item=="[":
            s.Push(item)
        
        elif item==")" or item=="}" or item=="]":
            if len(s.stk)==0:
                print("\nInvalid Expression")
            
            pop_item=s.stk[-1]
            
            if compare(pop_item,item):
                s.Pop()
            else:
                print("\nInvalid Expression")

if len(s.stk)==0:
    print("\nvalid Expression")
else:
    print("\nInvalid Expression")