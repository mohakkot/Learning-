from queue import PriorityQueue


class Astar:
    vertex = {}
    edge_cost = {}
    node_cost = {}

    def create_graph(self, list):
        type = list[0]
        start = list[1]
        goal = list[2]
        for i in range(1, int(list[3]) + 1):
            (front, next, cost) = list[i + 3].split()
            self.add_vertex(front, next, cost)
        node_no = list[int(list[3]) + 4]

        for i in range(1, int(node_no) + 1):
            (node, cost) = list[int(list[3]) + 4 + i].split()
            self.add_node_cost(node, cost)
        self.astar(start, goal)

    def add_vertex(self, front, next, cost):
        if front not in self.vertex.keys():
            self.vertex[front] = []
            self.vertex[front].append(next)
        else:
            self.vertex[front].append(next)
        self.edge_cost[str(front) + str(next)] = cost

    def add_node_cost(self, node, cost):
        self.node_cost[node] = cost

    def backtrack(self, parent, start, end):
        path = [end]
        distance = {}
        while path[-1] != start:
            temp = parent[path[-1]]
            adj = temp[0]
            amt = int(temp[1])
            value = self.vertex[adj]
            for nxt in value:
                if nxt == path[-1]:
                    path.append(adj)
                    distance[nxt] = amt
        distance[start]= 0
        path.reverse()
        fw = open('output.txt', 'w')
        for nodes in path:
            output = str(nodes) + ' ' + str(distance[nodes]) + '\n'
            fw.write(output)
        fw.close()

    def astar(self, start, goal):
        frontier = PriorityQueue()
        explored = {}
        path = {}
        pid = 0
        frontier.put((0, pid, start))
        from_node = {start:0}
        explored[start] = 0
        while frontier:
            cost, _, node = frontier.get()
            print(frontier.queue)
            if str(node) == str(goal):
                self.backtrack(path, start, goal)
                break
            if node in self.vertex.keys():
                value = self.vertex[node]
                for adj in value:
                    total_cost = cost + int(self.edge_cost[str(node) + str(adj)]) - int(from_node[node])
                    heuristics = total_cost + int(self.node_cost[adj])
                    if adj not in explored.keys() or (adj in explored.keys() and int(explored[adj]) > total_cost):
                        path[adj] = [node, total_cost]
                        pid = pid + 1
                        frontier.put((heuristics, pid, adj))
                        from_node[adj] = self.node_cost[adj]
                        explored[adj] = total_cost


class UCS:
    vertex = {}
    edge_cost = {}

    def create_graph(self, list):
        type = list[0]
        start = list[1]
        goal = list[2]
        for i in range(1, int(list[3]) + 1):
            (front, next, cost) = list[i + 3].split()
            self.add_vertex(front, next, cost)
        self.ucs(start, goal)

    def add_vertex(self, front, next, cost):
        if front not in self.vertex.keys():
            self.vertex[front] = []
            self.vertex[front].append(next)
        else:
            self.vertex[front].append(next)
        self.edge_cost[str(front) + str(next)] = cost

    def backtrack(self, parent, start, end):
        path = [end]
        distance = {}
        while path[-1] != start:
            temp = parent[path[-1]]
            adj = temp[0]
            amt = int(temp[1])
            value = self.vertex[adj]
            for nxt in value:
                if nxt == path[-1]:
                    path.append(adj)
                    distance[nxt] = amt
        distance[start] = 0
        path.reverse()
        fw = open('output.txt', 'w')
        for nodes in path:
            output = str(nodes) + ' ' + str(distance[nodes]) + '\n'
            fw.write(output)
        fw.close()

    def ucs(self, start, goal):
        frontier = PriorityQueue()
        explored = {}
        path = {}
        frontier.put((0, 0, start))
        pid = 0
        explored[start] = 0
        while frontier:
            cost, _, node = frontier.get()
            if str(node) == str(goal):
                self.backtrack(path, start, goal)
                break
            if node in self.vertex.keys():
                value = self.vertex[node]
                for adj in value:
                    total_cost = cost + int(self.edge_cost[str(node) + str(adj)])
                    if adj not in explored.keys() or (adj in explored.keys() and int(explored[adj]) > total_cost):
                    # path[adj] = [node, int(self.edge_cost[str(node) + str(adj)])]
                        path[adj] = [node, total_cost]
                        pid = pid + 1
                        frontier.put((total_cost, pid, adj))
                        explored[adj] = total_cost


class BFS:
    vertex = {}

    def create_graph(self, list):
        type = list[0]
        start = list[1]
        goal = list[2]
        for i in range(1, int(list[3]) + 1):
            (front, next, cost) = list[i + 3].split()
            self.add_vertex(front, next)
        self.bfs(start, goal)

    def add_vertex(self, front, next):
        if front not in self.vertex.keys():
            self.vertex[front] = []
            self.vertex[front].append(next)
        else:
            self.vertex[front].append(next)
        if next not in self.vertex.keys():
            self.vertex[next] = []
            self.vertex[next].append(front)


    def backtrack(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        fw = open('output.txt', 'w')
        distance = 0
        for nodes in path:
            output = str(nodes) + ' ' + str(distance) + '\n'
            fw.write(output)
            distance += 1
        fw.close()

    def bfs(self, start, goal):
        frontier = []
        explored = [start]
        path = {}
        frontier.append(start)
        while len(frontier) > 0:
            node = frontier.pop(0)
            if node == goal:
                self.backtrack(path, start, goal)
                break
            if node in self.vertex.keys():
                value = self.vertex[node]
                for adj in value:
                    if adj not in explored:
                        path[adj] = node
                        frontier.append(adj)
                        explored.append(adj)


class DFS:
    vertex = {}

    def create_graph(self, list):
        type = list[0]
        start = list[1]
        goal = list[2]
        for i in range(1, int(list[3]) + 1):
            (front, next, cost) = list[i + 3].split()
            self.add_vertex(front, next)
        self.dfs(start, goal)

    def add_vertex(self, front, next):
        if front not in self.vertex.keys():
            self.vertex[front] = []
            self.vertex[front].append(next)
        else:
            self.vertex[front].append(next)
        if next not in self.vertex.keys():
            self.vertex[next] = []
            self.vertex[next].append(front)

    def backtrack(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        fw = open('output.txt', 'w')
        distance = 0
        for nodes in path:
            output = str(nodes) + ' ' + str(distance) + '\n'
            fw.write(output)
            distance += 1
        fw.close()

    def dfs(self, start, goal):
        frontier = []
        explored = [start]
        path = {}
        frontier.append(start)
        while len(frontier) > 0:
            node = frontier.pop(-1)
            if node == goal:
                self.backtrack(path, start, goal)
                break
            if node in self.vertex.keys():
                value = self.vertex[node]
                value.reverse()
                for adj in value:
                    if adj not in explored:
                        path[adj] = node
                        frontier.append(adj)
                        explored.append(adj)


def file_read(file_name):
    fr = open(file_name, 'r')
    each_line = fr.readlines()
    line = [x.strip('\n') for x in each_line]
    if line[0] == 'BFS':
        ob = BFS()
        ob.create_graph(line)
    if line[0] == 'DFS':
        ob = DFS()
        ob.create_graph(line)
    if line[0] == 'UCS':
        ob = UCS()
        ob.create_graph(line)
    if line[0] == 'A*':
        ob = Astar()
        ob.create_graph(line)

    fr.close()


file_read('input.txt')
