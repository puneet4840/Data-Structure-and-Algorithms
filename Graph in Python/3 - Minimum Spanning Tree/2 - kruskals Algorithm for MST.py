# Kruskals Algorithm for Minimum Spanning Tree.
print()

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph=[]

    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])

    def find(self,parent,i):
        if parent[i]==i:
            return i
        else:
            return self.find(parent,parent[i])

    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)

        if rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1

    def Kruskals(self):
        result=[]
        k=0
        e=0

        self.graph=sorted(self.graph,key=lambda item:item[2])

        parent=[]
        rank=[]
        for i in range(self.vertices):
            parent.append(i)
            rank.append(0)

        while e<self.vertices-1:
            u,v,w=self.graph[k]
            k=k+1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e=e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)

        print('\nMinimum Spanning Tree')
        for s,d,w in result:
            print(f'{s} - {d} = {w}')

if __name__=='__main__':
    n=int(input('Enter the number of Vertices:  '))
    G=Graph(n)
    while True:
        print('\n=============')
        print('1: Insert Edge')
        print('2: Kruskals Algoithm')
        print('3: Exit')
        ch=int(input('Enter Your Choice:  '))

        if ch==1:
            s=int(input('Enter the Source Vertex: '))
            d=int(input('Enter Destination Vertex: '))
            w=int(input('Enter the Weight: '))
            G.add_edge(s,d,w)
        elif ch==2:
            G.Kruskals()
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')