# Detect Cycle in Undirected Graph using BFS(Bradth First Search) method.
print()

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph={}

        for vertex in self.vertices:
            self.graph[vertex]=[]

    def add_edge(self,s,d):
        if d in self.graph[s]:
            print(f'\nAlready an edge to {s} to {d}')
        else:
            self.graph[s].append(d)

    def delete_edge(self,s,d):
        if d not in self.graph[s]:
            print(f'\nNo edge between {s} to {d}')
        else:
            i=self.graph[s].index(d)
            self.graph[s].pop(i)

    def Print_Graph(self):
        for item in self.vertices:
            print(f'{item}-> {self.graph[item]}')

    def Detect_Cycle(self):
        in_degree=[0]*(len(self.vertices))
        queue=[]
        
        for item in self.vertices:
            for ele in self.graph[item]:
                in_degree[ele]+=1

        count=0

        for i in range(len(in_degree)):
            if in_degree[i]==0:
                queue.append(i)

        while len(queue)!=0:
            r_v=queue.pop(0)

            for neighbor in self.graph[r_v]:
                in_degree[neighbor]-=1
                
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
            count+=1

        if count==len(self.vertices):
            return False
        else:
            return True


if __name__=='__main__':
    nodes=[]
    n=int(input('Enter the number of nodes: '))
    for i in range(n):
        nodes.append(int(input(f'Enter vertex {i+1}: ')))

    G=Graph(nodes)
    while True:
        print('\n=========')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Detect Cycle')
        print('4: Display')
        print('5: Exit')
        ch=int(input('Enter Your Choice:  '))

        if ch==1:
            s=int(input('Enter Source Vertex: '))
            d=int(input('Enter Destination Vertex: '))
            G.add_edge(s,d)
        
        elif ch==2:
            s=int(input('Enter Source Vertex: '))
            d=int(input('Enter Destination Vertex: '))
            G.delete_edge(s,d)
        
        elif ch==3:
            result=G.Detect_Cycle()
            if result:
                print('\n Graph Contain Cycle')
            else:
                print('\n Graph does not Contain Cycle')
        
        elif ch==4:
            G.Print_Graph()

        elif ch==5:
            quit()

        else:
            print('\nInvalid Choice')