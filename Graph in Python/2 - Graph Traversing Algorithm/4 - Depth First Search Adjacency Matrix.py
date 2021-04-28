# Implementing Depth First Search using Adjacency Matrix.
print()

import numpy as np

class Graph:
    def __init__(self,size):
        self.size=size
        self.adj_mat=np.zeros((size,size),dtype=int)

    def add_edge(self,v1,v2):
        self.adj_mat[v1][v2]=1
        self.adj_mat[v2][v1]=1

    def delete_edge(self,v1,v2):
        if self.adj_mat[v1][v2]==0:
            print(f'\nNo edge between {v1} and {v2}')
        else:
            self.adj_mat[v1][v2]=0
            self.adj_mat[v2][v1]=0

    def Print_Graph(self):
        print(self.adj_mat)

    def Depth_First_Search(self,source):
        stack=[]
        visited=[0]*self.size
        stack.append(source)
        visited[source]=1
        # print(source,end='-')
        while len(stack)!=0:
            vertex=stack.pop(-1)
            print(vertex,end='-')
            for j in range(self.size):
                if self.adj_mat[vertex][j]==1 and visited[j]==0:
                    stack.append(j)
                    visited[j]=1

if __name__=='__main__':
    n=int(input('Enter the No. of Vertices: '))
    G=Graph(n)
    while True:
        print('\n===========')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: DFS')
        print('5: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            v1=int(input('Enter Source Vertex: '))
            v2=int(input("Enter Destination Vertex: "))
            G.add_edge(v1,v2)
        elif ch==2:
            v1=int(input("Enter Source Vertex: "))
            v2=int(input('Enter Destination Vertex: '))
            G.delete_edge(v1,v2)
        elif ch==3:
            G.Print_Graph()
        elif ch==4:
            s=int(input('Enter Source Vertex:  '))
            G.Depth_First_Search(s)
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')