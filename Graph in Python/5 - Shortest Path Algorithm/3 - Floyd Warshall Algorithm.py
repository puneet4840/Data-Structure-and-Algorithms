# Floyd Warshall Algorithm is an (All Pair Shortest Path Algorithm).
print()

import numpy as np

class Graph:
    def __init__(self,size):
        self.INF=9999
        self.size = size
        self.graph=np.zeros((size,size),dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                if i==j:
                    self.graph[i][j]=0
                else:
                    self.graph[i][j]=self.INF

    def add_edge(self,s,d,w):
        self.graph[s][d]=w

    def delete_edge(self,s,d,w):
        if self.graph[s][d]==self.INF:
            print(f'\nNo Direct Edge Between {s} and {d}')
        else:
            self.graph[s][d]=self.INF

    def Print_Graph(self):
        print(self.graph)

    def Floyd_Warshall(self,graph):
        
        # Below dist line is used to create the copy of self.graph.

        # dist=list(map(lambda i: list(map(lambda j: j,i)),graph))
        dist=self.graph
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

        print(dist)


if __name__=='__main__':
    n=int(input('Enter the number of Vertices:  '))
    G=Graph(n)
    while True:
        print('\n============')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: Floyd Warshall')
        # print('5: Display Floyd Warshall')
        print('5: Exit')
        ch=int(input('Enter Your Choice: '))

        if ch==1:
            s=int(input('Enter Source Vertex: '))
            d=int(input('Enter Destination Vertex: '))
            w=int(input('Enter the Weight:  '))
            G.add_edge(s,d,w)
        
        elif ch==2:
            s=int(input("Enter Source Vertex: "))
            d=int(input('Enter Destination Vertex: '))
            G.delete_edge(s,d)
        
        elif ch==3:
            G.Print_Graph()
        
        elif ch==4:
            G.Floyd_Warshall(G.graph)

        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')

