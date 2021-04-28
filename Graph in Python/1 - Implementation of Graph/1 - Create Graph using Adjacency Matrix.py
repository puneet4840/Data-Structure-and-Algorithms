# Creating Graph using Adjacency Matrix.
print()

import numpy as np


class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=np.zeros((size,size))

    def Add_Edge(self,v1,v2):
        self.graph[v1][v2]=1
        self.graph[v2][v1]=1
    
    def Delete_Edge(self,v1,v2):
        if self.graph[v1][v2]==0 and self.graph[v2][v1]==0:
            print('\nNo edge betwwen the vertex')
        else:
            self.graph[v1][v2]=0
            self.graph[v2][v1]=0

    def Print_Graph(self):
        print(self.graph)


if __name__=="__main__":
    num=int(input("Enter the number of vertices: "))
    G=Graph(num)
    while True:
        print('\n================================')
        print('1: Insert Edges (Connect Vertex)')
        print('2: Delete Edges (Disconnect Vertex)')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your choice:  "))

        if ch==1:
            v1,v2=input("Enter the space seperated two vertex: ").split()
            v1=int(v1)
            v2=int(v2)
            G.Add_Edge(v1,v2)
        elif ch==2:
            v1,v2=input("Enter the space seperated two vertex: ").split()
            v1=int(v1)
            v2=int(v2)
            G.Delete_Edge(v1,v2)
        elif ch==3:
            G.Print_Graph()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')