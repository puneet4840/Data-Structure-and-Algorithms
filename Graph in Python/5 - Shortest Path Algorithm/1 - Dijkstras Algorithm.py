# Dijkstra's Algorithm
print()

import numpy as np
import sys

class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=np.zeros((size,size),dtype=int)

    def add_edge(self,v1,v2,w):
        self.graph[v1][v2]=w
        self.graph[v2][v1]=w
        
    def delete_edge(self,v1,v2):
        if self.graph[v1][v2]==0:
            print(f'\nNo edge between {v1} and {v2}')
        else:
            self.graph[v1][v2]=0
            self.graph[v2][v1]=0

    def Print_Graph(self):
        print(self.graph)

    def min_distance(self,weight,visited):
        min=sys.maxsize

        for i in range(self.size):
            if weight[i]<min and visited[i]==False:
                min=weight[i]
                min_index=i
        return min_index

    def Dijkstra_Algo(self,source):

        weight=[sys.maxsize]*self.size
        weight[source]=0

        visited=[False]*self.size

        for i in range(self.size):
            u=self.min_distance(weight,visited)

            visited[u]=True

            for j in range(self.size):
                if self.graph[u][j]>0 and visited[j]==False and weight[j]>weight[u]+self.graph[u][j]:
                    weight[j]=weight[u]+self.graph[u][j]

        print(f'\nVertex ------ Distance from Source vertex {source}')
        for x in range(self.size):
            print(f'\t{source} to {x} ------ {weight[x]}')


if __name__=='__main__':
    size=int(input('Enter the number of nodes:  '))
    G=Graph(size)
    while True:
        print('\n=========')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Dijkstra Algorithm')
        print('4: Display')
        print('5: Exit')
        ch=int(input('Enter Your Choice: '))

        if ch==1:
            v1=int(input('Enter the Source Vertex: '))
            v2=int(input('Enter the Destination Vertex: '))
            w=int(input('Enter the Weight:  '))
            G.add_edge(v1,v2,w)
        elif ch==2:
            v1=int(input('Enter the Source Vertex: '))
            v2=int(input("Enter the Destination Vertex: "))
            G.delete_edge(v1,v2)
        elif ch==3:
            s=int(input('Enter the Source Vertex: '))
            G.Dijkstra_Algo(s)
        elif ch==4:
            G.Print_Graph()
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')
