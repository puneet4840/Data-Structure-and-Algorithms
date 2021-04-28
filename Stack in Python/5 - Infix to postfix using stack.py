# Parenthesis free expressions are called Polish Notation.
## Infix Notation: A+B
## Postfix Notation: AB+
## Prefix Notation: +AB

# Here we are converting the Infix Notation to Postfix Notation.
print()

class Stack():
    def __init__(self):
        self.stk=list()

    def Push(self,item):
        self.stk.append(item)

    def Pop(self):
        return self.stk.pop(-1)

infix=list()
x=input("Enter the Infix Expression:  ")
for i in x:
    infix.append(str(i))
postfix=list()
    
s=Stack()
s.Push("(")
infix.append(str(')'))

if __name__ == "__main__":

    def precedence(char):
        if char=="*" or char=="/":
            return 1
        elif char=="+" or char=="-":
            return 2
        else:
            return 3

    for ele in infix:
        if len(s.stk)==0:
            break
        else:
            if ele.isalpha():
                postfix.append(str(ele))
            elif ele=="(" or ele=="{" or ele=="[":
                s.Push(str(ele))
            elif ele=='*' or ele=='/' or ele=='+' or ele=='-':
                ed_ele=s.stk[-1]
                result=precedence(ed_ele)
                if result==2 or result==1:
                    s.Pop()
                elif result==3:
                    s.Push(str(ele))
            elif ele==")" or ele=="}" or ele=="]":
                while True:
                    p_e=s.Pop()
                    if p_e=="(" or p_e=="{" or p_e=="[":
                        break
                    else:
                        postfix.append(str(p_e))

# print(infix)
print("Postfix Expression:\n")
for item in postfix:
    print(f"{item}",end="")
print()