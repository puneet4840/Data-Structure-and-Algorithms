# Priority Queue is a special type of queue in DS in which high priority elements are removed first then normal.
print()

class PQueue():
    def __init__(self):
        self.pque=list()
        self.size=int(input("Enter the size of queue: "))
        print("\nPriority: Smallest number highest priority")

    def Enqueue(self,item):
        if len(self.pque)==self.size:
            print("\nPriority Queue is Full")

        else:
            self.pque.append(item)

    def Dequeue(self):
        if len(self.pque)==0:
            print("Priority Queue is Empty")

        else:
            min=0
            for i in range(len(self.pque)):
                if self.pque[i]<self.pque[min]:
                    min=i
            self.pque.pop(min)

    def Display(self):
        if len(self.pque)==0:
            print("\nPriority Queue is Empty")
        
        else:
            print("\nPriority Queue:")
            for i in range(len(self.pque)):
                print(f"{self.pque[i]}",end="-")
    

if __name__ == "__main__":

    pq=PQueue()

    while True:
        print('==============')
        print('\n1: Enqueue')
        print('2: Dequeue')
        print('3: Display')
        print('4: Exit')
        n=int(input("Enter your choice:  "))
        if n==1:
            item=int(input("Enter the element:  "))
            pq.Enqueue(item)

        elif n==2:
            pq.Dequeue()

        elif n==3:
            pq.Display()
        
        elif n==4:
            quit()

        else:
            print("\nInvalid Choice")
