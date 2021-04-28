# Implementing the Breadth First Search(BFS) using Adjacency List.
print()

from queue import Queue

class Graph:
    def __init__(self,nodes):
        self.vertices=nodes
        self.adj_list={}

        for vertex in self.vertices:
            self.adj_list[vertex]=[]

    def add_edge(self,s,d):
        self.adj_list[s].append(d)
        self.adj_list[d].append(s)

    def delete_edge(self,s,d):
        if d not in self.adj_list[s]:
            print(f'\n no edge between {s} and {d}')
        else:
            i1=self.adj_list[s].index(d)
            self.adj_list[s].pop(i1)
            i2=self.adj_list[d].index(s)
            self.adj_list[d].pop(i2)

    def Print_Graph(self):
        for item in self.adj_list:
            print(item,'->',self.adj_list[item])

    def Breadth_First_Search(self,source):
        Q=Queue()
        visited=[]
        Q.put(source)
        while not Q.empty():
            vertex=Q.get()
            if vertex in visited:
                continue
            print(vertex,end='-')
            visited.append(vertex)
            for item in self.adj_list[vertex]:
                Q.put(item)
                


if __name__=='__main__':
    nodes=[]
    n=int(input('Enter the no. of Vertices: '))
    for i in range(n):
        nodes.append(int(input(f'Enter vertex {i+1}:  ')))
    G=Graph(nodes)
    while True:
        print('\n===============')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: BFS')
        print('5: Exit')
        ch=int(input('Enter Your Choice: '))

        if ch==1:
            s=int(input('Enter the Source Vertex: '))
            d=int(input("Enter the Destination Vertex: "))
            G.add_edge(s,d)
        elif ch==2:
            s=int(input('Enter the Source Vertec: '))
            d=int(input("Enter the Destination Vertex: "))
            G.delete_edge(s,d)
        elif ch==3:
            G.Print_Graph()
        elif ch==4:
            s=int(input('Enter the Source Vertex:  '))
            G.Breadth_First_Search(s)
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')