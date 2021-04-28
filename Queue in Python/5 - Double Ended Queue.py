# Double Ended Queue: When insertion and Deletion can be done on both (rear and front) ends.
# It is called Double Ended Queue or Deque.
print()


class Dequeue():
    def __init__(self):
        self.size=int(input("Enter the szie of Dequque:  "))
        self.Deque=list()

    def Insert_from_rear_side(self,item):
        if len(self.Deque)==self.size:
            print("\nDequeue is Full")
        else:
            self.Deque.append(item)
        
    def Insert_from_Front_side(self,item1):
        if len(self.Deque)==self.size:
            print("\nDequeue is Full")
        else:
            self.Deque.insert(0,item1)

    def Delete_from_front(self):
        if len(self.Deque)==0:
            print("\nDequeue is Empty")
        else:
            self.Deque.pop(0)

    def Delete_from_rear(self):
        if len(self.Deque)==0:
            print("\nDequeue is Empty")
        else:
            self.Deque.pop(-1)

    def Front(self):
        if len(self.Deque)==0:
            print("\nDequeue is Empty")
        else:
            print(self.Deque[0])
    
    def Rear(self):
        if len(self.Deque)==0:
            print("\nDequeue is Empty")
        else:
            print(self.Deque[-1])

    def Display(self):
        if len(self.Deque)==0:
            print("\nDequeue is Empty")
        else:
            print()
            for i in self.Deque:
                print(i,end="<-")
            print()


if __name__ == "__main__":
    dq=Dequeue()

    while True:
        print("===========================")
        print('\n1: Insert from rear side')
        print('2: Insert from front side')
        print('3: Delete from front side')
        print('4: Delete from rear side')
        print('5: Front Element')
        print('6: Rear Element')
        print('7: Display')
        print('8: Exit')
        n=int(input("Enter your choice:  "))
        if n==1:
            dq.Insert_from_rear_side(int(input("Enter the Element:  ")))
        elif n==2:
            dq.Insert_from_Front_side(int(input("Enter the Element:  ")))
        elif n==3:
            dq.Delete_from_front()
        elif n==4:
            dq.Delete_from_rear()
        elif n==5:
            dq.Front()
        elif n==6:
            dq.Rear()
        elif n==7:
            dq.Display()
        elif n==8:
            quit()
        else:
            print('\nInvalid Choice')
