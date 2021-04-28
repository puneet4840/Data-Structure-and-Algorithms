# Queue is the ordered collection of items which follows the FIFO (First In First Out) rule.
## Insertion is done at rear end of the queue and Deletion is done at front end of the queue.
print()


class Queue():
    def __init__(self):
        self.size=int(input("\nEnter the size of the Queue: "))
        self.que=list()

    def Enqueue(self,item):
        if len(self.que)==self.size:
            print("\n>>>> Queue is Full")
        else:
            self.que.append(item)

    def Dequeue(self):
        if len(self.que)==0:
            print("\n>>>> Queue is Empty")
        else:
            self.que.pop(0)

    def Front(self):
        if len(self.que)==0:
            print("\n>>>> Queue is Empty")
        else:
            print(f"\nFront: {self.que[0]}")
        
    def Rear(self):
        if len(self.que)==0:
            print("\n>>>> Queue is Empty")
        else:
            print(f"\nRear: {self.que[-1]}")
        
    def Display(self):
        if len(self.que)==0:
            print("\n>>>> Queue is Empty")
        else:
            print("Queue -->")
            for item in self.que:
                print(f"{item} <-- ",end=" ")


if __name__ == "__main__":
    q=Queue()

    while True:
        print("\n------------------")
        print("\n1: Enqueue")
        print("\n2: Dequeue")
        print("\n3: Front Element")
        print("\n4: Rear Element")
        print("\n5: Display the Queue")
        print("\n6: Exit")
        x=int(input("\nEnter your Choice:  "))

        if x==1:
            item=int(input("\nEnter the element: "))
            q.Enqueue(item)
        
        elif x==2:
            q.Dequeue()

        elif x==3:
            q.Front()

        elif x==4:
            q.Rear()
        
        elif x==5:
            q.Display()
        
        elif x==6:
            quit()
        else:
            print("\nInvalid Choice\n")