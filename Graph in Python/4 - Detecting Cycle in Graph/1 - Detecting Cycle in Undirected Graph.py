# Detect Cycle in Undirected Graph using DFS.
print()

class Graph:
    def __init__(self,vertex):
        self.vertices=vertex
        self.graph={}

        for vertex in self.vertices:
            self.graph[vertex]=[]

    def add_edge(self,s,d):
        self.graph[s].append(d)
        self.graph[d].append(s)

    def Delete_edge(self,s,d):
        if d not in self.graph[s]:
            print(f'\n No edge between {s} and {d}')
        else:
            i1=self.graph[s].index(d)
            self.graph[s].pop(i1)
            i2=self.graph[d].index(s)
            self.graph[d].pop(i2)

    def Print_Graph(self):
        for item in self.vertices:
            print(f'{item}: {self.graph[item]}')

    def isCyclicUtil(self,v,visited,parent):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if self.isCyclicUtil(i,visited,v)==True:
                    return True
            elif parent!=i:
                return True
        return False
        
    def Detect_Cycle(self):
        visited=[False]*(len(self.vertices))
        for i in range(len(self.vertices)):
            if visited[i]==False:
                if self.isCyclicUtil(i,visited,-1)==True:
                    return True
        return False


if __name__=='__main__':
    nodes=[]
    n=int(input('Enter the Number of Element:  '))
    for i in range(n):
        nodes.append(int(input(f'Enter Element {i+1}: ')))

    G=Graph(nodes)
    while True:
        print('\n============')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Detect Cycle')
        print('4: Display')
        print('5: Exit')
        ch=int(input('Enter Your Choice: '))

        if ch==1:
            s=int(input('Enter the Source Vertex: '))
            d=int(input('Enter the Destination Vertex: '))
            G.add_edge(s,d)
        elif ch==2:
            s=int(input('Enter the Source Vertex: '))
            d=int(input('Enter the Destination Vertex: '))
            G.Delete_edge(s,d)
        elif ch==3:
            re=G.Detect_Cycle()
            if re:
                print('\nCycle is Found in Graph')
            else:
                print('\nCycle Not Found')
        elif ch==4:
            G.Print_Graph()
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')