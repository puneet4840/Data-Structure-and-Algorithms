# Node contains two fields: 
## 1: Data
## 2: Next
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

temp1=Node(10)
temp2=Node(20)
print(temp1)
print(f"Data: {temp1.data}")
print(f"Next: {temp1.next}")
print()

temp1.next=temp2
ptr=temp1
print(ptr.data,end="->")
ptr=ptr.next
print(ptr.data)