class Vertex:
    def __init__(self, n):
        self.name= n
        self.neighbors = list()
        self.distance = 9999
        #self.color = 'black'

    def add_neighbor(self, v, cost=0):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors[v] = cost
            self.neighbors.sort()

    def __str__(self):
        return str(self.id) + 'joined with: ' + str([a.id for a in self.neighbors])

    def  getconnections(self):
        return self.neighbors.keys()

    def showcost(self, u):
        return self.neighbors[u]

class Graph:
    vertices = {}

    def add_vertex(self,  vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, cost =0):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v, cost)
                if key == v:
                    value.add_neighbor(u, cost)
            return True
        else:
            return False


class Read_file():

    def file_read(self, file_name):
        fr = open(file_name, 'r')
        each_line = fr.readlines()
        print(each_line)
        line = [x.split('\n')[0] for x in each_line]
        print(line)
        #self.assign_val(line)
        self.file_dict(line)
        print(line[::3])

    def file_dict(self, file_name):
        d= dict()
        with open(file_name) as fr:
            for line in fr:
                (key, val, cost) = line.split()
                print(key, val, cost)
                if key in d.keys():
                    d[key][val] = cost
                else:
                    d[key] = {}
                    d[key][val] = cost
            print(d)
        g= [d]
        print(g)



fr = Read_file()
fr.file_dict('sample1.txt')