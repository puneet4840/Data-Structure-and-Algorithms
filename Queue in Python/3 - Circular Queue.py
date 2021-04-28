# # Cicular queue is used when we dont want sifting of elements after deletion in simple queue.
# print()


# class Cqueue():
#     def __init__(self):
#         self.size=int(input("Enter the size of the queue:  "))
#         self.que=[None]*self.size
#         self.front=self.rear=-1

#     def Enqueue(self,item):
#         if ((self.rear+1)%self.size==self.front):
#             print("\nQueue is Full")
        
#         elif self.front==-1:
#             rear=0
#             front=0
#             self.que[self.rear]=item

#         else:
#             self.rear=(self.rear+1)%self.size
#             self.que[self.rear]=item

#     def Dequeue(self):
#         if self.front==-1:
#             print("\nQueue is Empty")
        
#         elif self.front==self.rear:
#             self.que.pop(self.front)
#             self.front=-1
#             self.rear=-1

#         else:
#             self.que.pop(self.front)
#             self.front=(self.front+1)%self.size

#     def Display(self):
#         if self.front==-1:
#             print("\nQueue is Empty")

#         elif self.rear>=self.front:
#             for i in range(self.front,self.rear+1):
#                 print(self.que[i],end=" ")
            
#         elif (self.rear+1)%self.size==self.front:
#             print("\nQueue is Full")

#         else:
#             print("Circular Queue: \n")
#             for i in range(self.front,self.size):
#                 print(self.que[i],end=" ")

#             for j in range(0,self.rear+1):
#                 print(self.que[j],end=" ")


# if __name__ == "__main__":

#     q=Cqueue()

#     while True:
#         print('\n1: Enqueue')
#         print('\n2: Dequeue')
#         print('\n3: Display')
#         print('\n4: Exit')
#         n=int(input("\nEnter your choice:  "))

#         if n==1:
#             item=int(input("Enter the element:  "))
#             q.Enqueue(item)

#         elif n==2:
#             q.Dequeue()

#         elif n==3:
#             q.Display()

#         elif n==4:
#             quit()

#         else:
#             print("\nInvalid Choice")

