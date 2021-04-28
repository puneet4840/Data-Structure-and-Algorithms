# Prim's Algorithm to find Minimum Spanning Tree.
print()
import numpy as np
import sys

class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=np.zeros((size,size),dtype=int)
        self.min=sys.maxsize

    def add_edge(self,v1,v2,w):
        if self.graph[v1][v2]>0:
            print('\nAlready an Edge')
        else:
            self.graph[v1][v2]=w
            self.graph[v2][v1]=w

    def delete_edge(self,v1,v2):
        if self.graph[v1][v2]==0:
            print('\n No edge between ',v1,' and ',v2)
        else:
            self.graph[v1][v2]=0
            self.graph[v2][v1]=0

    def Print_graph(self):
        print(self.graph)

    def Prims_Algo(self,source):
        weight=[self.min]*self.size
        visited=[False]*self.size
        result=[None]*self.size
        weight[source]=0
        result[source]=-1
        for cout in range(self.size):
            for v in range(self.size):
                self.min=sys.maxsize
                if weight[v]<self.min and visited[v]==False:
                    self.min=weight[v]
                    min_index=v
            visited[min_index]=True
            for v in range(self.size):
                if self.graph[min_index][v]>0 and visited[v]==False and weight[v]>self.graph[min_index][v]:
                    weight[v]=self.graph[min_index][v]
                    result[v]=min_index
        
        self.Display_Prims(result)

    def Display_Prims(self,result):
        print('\nEdge  =   Weight')
        for i in range(1,self.size):
            print(result[i], '-', i, '\t', self.graph[i][result[i]])


if __name__=='__main__':
    n=int(input('Enter the number of Vertices: '))
    G=Graph(n)
    while True:
        print('\n=================')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: PRIM"S ALGORITHM ')
        print('5: Exit')
        ch=int(input('Enter Your Choice: '))

        if ch==1:
            v1=int(input('Enter Source Vertex:  '))
            v2=int(input('Enter Destination Vertex:  '))
            w=int(input('Enter the Weight: '))
            G.add_edge(v1,v2,w)
        elif ch==2:
            v1=int(input('Enter Source Vertex:  '))
            v2=int(input('Enter Destination Vertex:  '))
            G.delete_edge(v1,v2)
        elif ch==3:
            G.Print_graph()
        elif ch==4:
            source=int(input('Enter the Source Vertex:  '))
            G.Prims_Algo(source)
        elif ch==5:
            quit()
        else:
            print('\n Invalid Choice')