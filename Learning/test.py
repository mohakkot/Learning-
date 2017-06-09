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
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in graph.get(node, []):
            parent[adjacent] = node # <<<<< record its parent
            queue.append(adjacent)


def file_dict(self, file_name):
    d = dict()
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
    g = [d]
    print(g)

file_dict ('sample.txt')