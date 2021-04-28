# Depth First Search using Adjacency List.
print()

class Graph:
    def __init__(self,nodes):
        self.vertices=nodes
        self.adj_lst={}

        for vertex in self.vertices:
            self.adj_lst[vertex]=[]

    def add_edge(self,s,d):
        self.adj_lst[s].append(d)
        self.adj_lst[d].append(s)

    def delete_edge(self,s,d):
        if d not in self.adj_lst[s]:
            print('\nNo edge between',s,d)
        else:
            i1=self.adj_lst[s].index(d)
            self.adj_lst[s].pop(i1)
            i2=self.adj_lst[d].index(s)
            self.adj_lst[d].pop(i2)

    def Print_Graph(self):
        for item in self.vertices:
            print(item,'->',self.adj_lst[item])

    def Depth_First_Search(self,source):
        stack=[]
        visited=[]
        stack.append(source)
        while len(stack)!=0:
            vertex=stack.pop(-1)
            if vertex in visited:
                continue
            print(vertex,end='-')
            visited.append(vertex)
            for item in self.adj_lst[vertex]:
                if item not in visited:
                    stack.append(item)


if __name__=='__main__':
    nodes=[]
    n=int(input("Enter the NO. of Vertices:  "))
    for i in range(n):
        nodes.append(int(input(f'Enter Vertex {i+1}: ')))

    G=Graph(nodes)
    while True:
        print('\n=============')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: DFS')
        print('5: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            s=int(input('Enter Source Vertex:  '))
            d=int(input('Enter Destination Vertex:  '))
            G.add_edge(s,d)
        elif ch==2:
            s=int(input("Enter Source Vertex:  "))
            d=int(input("Enter Destination Vertex:  "))
            G.delete_edge(s,d)
        elif ch==3:
            G.Print_Graph()
        elif ch==4:
            s=int(input("Enter the Source Vertex: "))
            G.Depth_First_Search(s)
        elif ch==5:
            quit()
        else:
            print('\nInvalid Choice')