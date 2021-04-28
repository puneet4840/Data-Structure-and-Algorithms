# Bellman Ford Algorithm in python.
print()

import sys

class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=[]

    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])

    def print_graph(self):
        print()
        print('Source \t Weight \t Destination')
        for s,d,w in self.graph:
            print(f'{s} \t {w} \t\t {d}')

    def Display_Bellman_Ford(self,dist,source):
        print()
        print(f'Vertex \t Distance From Source Vertex {source}')
        for i in range(len(dist)):
            print(f'{i} \t {dist[i]}')

    def Bellman_Ford(self,source):
        dist=[sys.maxsize]*self.size
        dist[source]=0

        for _ in range(self.size-1):
            for s,d,w in self.graph:
                if dist[s]!=sys.maxsize and dist[s]+w<dist[d]:
                    dist[d]=dist[s]+w
        
        self.Display_Bellman_Ford(dist,source)

if __name__=='__main__':
    n=int(input('Enter the number of Vertices: '))
    G=Graph(n)
    while True:
        print('\n============')
        print('1: Insert Edge')
        print('2: Dijkstra Algorithm')
        print('3: Display')
        print('4: Exit')
        ch=int(input('Enter Your Choice:  '))

        if ch==1:
            s=int(input('Enter the Source Vertex: '))
            d=int(input('Enter the Destination Vertex: '))
            w=int(input('Enter the Weight: '))
            G.add_edge(s,d,w)
        
        elif ch==2:
            source=int(input('Enter the Source vertex: '))
            G.Bellman_Ford(source)

        elif ch==3:
            G.print_graph()

        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')