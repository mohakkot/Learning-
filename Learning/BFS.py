def file_read(file_name):
    fr = open(file_name, 'r')
    each_line = fr.readlines()
    #print(each_line)
    line = [x.strip('\n') for x in each_line]
    #print(line)
    create_graph(line)



def create_graph(list):
    type = list[0]
    start = list[1]
    goal = list[2]
    d = {}
    for i in range(1, int(list[3]) + 1):
        (key, val, cost) = list[i + 3].split()
        #print(key, val, cost)
        if key in d.keys():
            d[key][val] = cost
        else:
            d[key] = {}
            d[key][val] = cost
        #print(d)
    g = [d]
    print(g)
    print(type)
    print(bfs(g, start, goal))

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
       path.append(parent[path[-1]])
       path.reverse()
       return path

def bfs(graph, start, end):
    parent = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node)
        if node == end:
           return backtrace(parent, start, end)
        print(graph)
        for data in graph:
            print(data)
            data[val.keys()] = next_node
               parent[next_node] = node  # <<<<< record its parent
               queue.append(next_node)


file_read('sample.txt')