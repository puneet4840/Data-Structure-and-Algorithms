# Creating Directed Graph using Adjacency List.
print()

class Graph:
    def __init__(self,nodes):
        self.vertices=nodes
        self.adj_list={}

        for vertex in self.vertices:
            self.adj_list[vertex]=[]

    def add_edge(self,s,d):
        self.adj_list[s].append(d)

    def delete_edge(self,s,d):
        if d not in self.adj_list[s]:
            print(f'\nNo edge between {s} to {d}')
        else:
            i=self.adj_list[s].index(d)
            self.adj_list[s].pop(i)

    def Print_Graph(self):
        if len(self.vertices)==0:
            print('\nGraph is Empty')
        else:
            for item in self.vertices:
                print(item,' -> ',self.adj_list[item])

if __name__=="__main__":
    nodes=[]
    n=int(input('Enter the No. of Vertices:  '))
    for i in range(n):
        nodes.append(int(input(f'Enter vertex {i+1}: ')))
    G=Graph(nodes)
    while True:
        print('\n======================')
        print('1: Insert Edge')
        print('2: Delete Edge')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            s=int(input('Enter Source Vertex:  '))
            d=int(input("Enter Destination Vertex:  "))
            G.add_edge(s,d)
        elif ch==2:
            s=int(input("Enter Source Vertex: "))
            d=int(input("Enter Destination Vertex:  "))
            G.delete_edge(s,d)
        elif ch==3:
            G.Print_Graph()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')