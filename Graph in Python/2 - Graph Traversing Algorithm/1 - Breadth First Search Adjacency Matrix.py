# Breadth First Search(BFS) using Adjacnecy Matrix.
## Undirected Graph

print()
import numpy as np
from queue import Queue

class Graph:
    def __init__(self,size):
        self.size=size
        self.adj_mat=np.zeros((size,size),dtype=int)

    def add_edge(self,v1,v2):
        self.adj_mat[v1][v2]=1
        self.adj_mat[v2][v1]=1

    def delete_edge(self,v1,v2):
        if self.adj_mat[v1][v2]==0:
            print(f'\n No edge between {v1} and {v2}')
        else:
            self.adj_mat[v1][v2]=0
            self.adj_mat[v2][v1]=0

    def Print_graph(self):
        if len(self.adj_mat)==0:
            print('\n Graph is Empty')
        else:
            print(self.adj_mat)
    
    def Breadth_First_Search(self,source):
        Q=Queue()
        visited=[0]*self.size
        i=source
        Q.put(i)
        visited[i]=1
        print(i,end='-') 
        while not Q.empty():
            i=Q.get()
            for j in range(self.size):
                if self.adj_mat[i][j]==1 and visited[j]==0:
                    print(j,end='-')
                    Q.put(j)
                    visited[j]=1


if __name__=="__main__":
    n=int(input('Enter the number of Vertices:  '))
    G=Graph(n)
    while True:
        print('\n=============')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: BFS')
        print('5: Exit')
        ch=int(input('Enter Your Choice:  '))

        if ch==1:
            v1=int(input('Enter Source Vertex: '))
            v2=int(input('Enter Destination Vertex:  '))
            G.add_edge(v1,v2)
        elif ch==2:
            v1=int(input('Enter Source Vertex:  '))
            v2=int(input('Enter Desitination Vertex:  '))
            G.delete_edge(v1,v2)
        elif ch==3:
            G.Print_graph()
        elif ch==4:
            s=int(input('Enter the Source Vertex:  '))
            G.Breadth_First_Search(s)
        elif ch==5:
            quit()
        else:
            print('\n Invalid Choice')