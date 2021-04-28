# Creating Weighted Graph using Adjacency Matrix.
print()

import numpy as np

class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=np.zeros((size,size),dtype=int)

    def add_edge(self,v1,v2,weight):
        self.graph[v1][v2]=weight

    def delete_edge(self,v1,v2):
        if self.graph[v1][v2]==0:
            print(f'\nNo edge between {v1} and {v2}')
        else:
            self.graph[v1][v2]=0
        
    def Print_graph(self):
        if len(self.graph)==0:
            print('\nGraph is Empty')
        else:
            print(self.graph)


if __name__=='__main__':
    n=int(input('Enter the No. of Vertices:  '))
    G=Graph(n)
    while True:
        print('\n===============')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: Exit')
        ch=int(input('Enter Your Choice:  '))

        if ch==1:
            v1=int(input('Enter the Source Vertex: '))
            v2=int(input('Enter the Destination Vertex: '))
            w=int(input('Enter the Weight of Vertices: '))
            G.add_edge(v1,v2,w)
        elif ch==2:
            v1=int(input('Enter the Source Vertex: '))
            v2=int(input('Enter the Destination Vertex: '))
            G.delete_edge(v1,v2)
        elif ch==3:
            G.Print_graph()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')