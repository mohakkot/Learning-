class Vertex:
    def __init__(self, n):
        self.name= n
        self.neighbors = list()
        self.distance = 9999
        #self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            #self.neighbors[v] = cost
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self,  vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in self.vertices.keys():
            print (key + ":" + str(self.vertices[key].neighbors))

    def get(self, node):
        adj = []
        print(self.vertices)
        adj.append(self.neighbors[node])
        print(adj)

def file_read(file_name):
    fr = open(file_name, 'r')
    each_line = fr.readlines()
    #print(each_line)
    line = [x.strip('\n') for x in each_line]
    #print(line)
    create_graph(line)
    fr.close()


def create_graph(list):
    type = list[0]
    start = list[1]
    goal = list[2]
    for i in range(1, int(list[3]) + 1):
        (front, next, cost) = list[i + 3].split()
        #print(front, next)
        g = Graph()
        g.add_vertex(Vertex(front))
        g.add_vertex(Vertex(next))
        g.add_edge(front, next)
    #print(g.print_graph())
    bfs(g, start, goal)


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
       path.append(parent[path[-1]])
       path.reverse()
       print(path)

def bfs(graph, start, goal):
    path = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == goal:
            return backtrace(path, start, goal)
        graph.get(node)
        for adj in :
            path[adj] = node
            queue.append(adj)


file_read('sample.txt')