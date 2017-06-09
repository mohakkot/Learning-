import queue
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    q = []
    # push the first path into the queue
    q.append([start])
    while q:
        #print(q)
        # get the first path from the queue
        path = q.pop(0)
        #print(path)
        # get the last node from the path
        node = path[-1]
        #print(node)
        # path found
        if node == end:
            print(path)
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            print(adjacent)
            new_path = list(path)
            print(new_path)
            new_path.append(adjacent)
            q.append(new_path)
            print(new_path)

bfs(graph, '1', '11')

