import time
from tqdm import tqdm
from collections import defaultdict
import heapq
import numpy as np
from matplotlib import pyplot as plt


class Graph:  # class that does it all
    def __init__(self, graph):
        self.graph = graph
        self.parent = {}
        self.rank = {}

    #==================================================================#

    def prim(self, source='a'):
        """ Func to find the MST via Prim's algorithm """

        print("\n=============================")
        print("MST with Prim's Algorithm\n")

        # asking for source, getting valid input
        choice = input("Default source node = 'a', change? [Y/N]: ").lower()
        if choice == 'y':
            while True:  # loop to get valid input
                source = input(f"\nEnter source node {set(self.graph.keys())}: ")
                if (source.isalpha()) and (source.lower() in self.graph.keys()):  # check if alpha and in graph
                    source = source.lower()
                    break
                else:
                    print('Enter valid input from {}\n'.format(
                        list(self.graph.keys())))

        print(f"Start from = {source}")
        path = defaultdict(set)  # tree path
        visited = [source]
        # automatically making the vertex from node goal node and coupling in their respective weight
        vertex = [(weight, source, goal)
                  for goal, weight in self.graph[source].items()]
        # automatically prioritize node with smallest weight
        heapq.heapify(vertex)

        while vertex:  # looping until vertex heap is empty
            # print(vertex)
            weight, start, goal = heapq.heappop(vertex)
            if goal not in visited:  # storing nodes that are visited
                visited.append(goal)
                path[start].add(goal)  # adding the children of nodes
                for next, weight in self.graph[goal].items():
                    if next not in visited:  # add unvisited nodes and their weight to the heap
                        heapq.heappush(vertex, (weight, goal, next))

        # pairing start and destinations
        path = list(zip(list(path.keys()), list(path[x] for x in path.keys())))

        # pretty printing the result
        time.sleep(0.2)
        for keys, values in path:
            print(f"From {keys} -> {values}")
            time.sleep(0.2)

    #==================================================================#

    def find(self, v):
        """ Func to find the root of an element in a set """
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, v, u):
        """ Func to join 2 subsets """
        first = self.find(v)  # finding the root of both nodes
        second = self.find(u)

        # find the smaller weight node
        if self.rank[first] > self.rank[second]:
            self.parent[second] = first
        else:
            self.parent[first] = second
            if self.rank[first] == self.rank[second]:
                self.rank[second] += 1

    def kruskal(self):
        """ Func to construct MST using Kruskal's algorithm """
        for v in self.graph.keys():
            self.parent[v] = v
            self.rank[v] = 0

        vertexs = []  # storing vertices
        path = []  # storing path result

        for out_key in self.graph.keys():  # iterating through children of nodes
            for in_key, in_key_weight in self.graph[out_key].items():
                vertexs.append((in_key_weight, out_key, in_key))

        vertexs.sort()

        for vertex in vertexs:  # to find path with no cycles
            weight, v, u = vertex

            if self.find(v) != self.find(u):  # closed loop checker
                self.union(v, u)
                path.append(vertex)
        print("\n=============================")
        print("MST with Kruskal algorithm\n")
        for x in range(len(path)):
            print(f"{path[x][1]} to {path[x][2]} -> {path[x][0]}")
            time.sleep(0.2)
        time.sleep(0.2)
        print(f"\nTotal Weight -> {np.sum([x[0] for x in path])}")
        time.sleep(0.2)
        return ''

    #==================================================================#

    def show_graph(self):
        """ Func to pretty print out the nodes and it's children along with the each of their weight """
        print('Graph:')
        keys = list(self.graph.keys())
        for key in keys:
            sub_keys = list(self.graph[key].keys())
            for sub_key in sub_keys:
                if sub_key == sub_keys[0]:
                    print('-----------')
                    print(f'{key} -> {sub_key} = {self.graph[key][sub_key]}')
                    time.sleep(0.2)
                else:
                    print(
                        f"{' ' * len(f'{key} -> ')}{sub_key} = {self.graph[key][sub_key]}")
                    time.sleep(0.2)

        print('-----------')

        # storing the points for the nodes
        points = [[1, 2],
                  [2, 3], [2, 1],
                  [3, 2],
                  [4, 1], [4, 3],
                  [5, 1], [5, 3],
                  [6, 2]]

        def edge(x, y):
            """ Func to plot the vertices between nodes """
            plt.plot(x, y, color='red',
                     linewidth=5, alpha=0.7, zorder=1)

        def tag(x, y, tag, color='white'):
            """ Func to plot the nodes and the necessary tags for the graph """
            plt.text(x, y, tag, fontdict={'color': color, 'size': 20},
                     horizontalalignment='center', verticalalignment='center')

        plt.figure()  # plotting the graph on matplotlib
        plt.style.use('fivethirtyeight')

        # vertices
        edge([1, 2], [2, 1])
        edge([1, 2], [2, 3])
        edge([2, 2], [1, 3])
        edge([2, 3], [1, 2])
        edge([2, 4], [3, 3])
        edge([3, 4], [2, 3])
        edge([2, 2], [1, 1])
        edge([2, 4], [1, 1])
        edge([3, 4], [2, 1])
        edge([4, 5], [1, 1])
        edge([4, 5], [3, 1])
        edge([4, 5], [3, 3])
        edge([5, 5], [1, 3])
        edge([5, 6], [1, 2])
        edge([5, 6], [3, 2])

        # nodes
        plt.scatter([x[0] for x in points],
                    [x[1] for x in points],
                    s=1800, c='black', zorder=2, edgecolor='blue', linewidth=5)

        # node tags
        node_tags = list(self.graph.keys())
        for point in range(len(points)):
            tag(points[point][0], points[point][1], node_tags[point])

        # weight tags
        tag(1.4, 1.4, 8, 'black')
        tag(1.4, 2.65, 4, 'black')
        tag(1.8, 2, 11, 'black')
        tag(3, 1.1, 1, 'black')
        tag(2.7, 1.5, 7, 'black')
        tag(3.3, 1.5, 6, 'black')
        tag(3, 2.9, 8, 'black')
        tag(3.3, 2.5, 2, 'black')
        tag(4.5, 2.9, 7, 'black')
        tag(4.8, 2, 14, 'black')
        tag(4.3, 2, 4, 'black')
        tag(5.3, 2.5, 6, 'black')
        tag(4.5, 1.1, 2, 'black')
        tag(5.3, 1.5, 10, 'black')

        plt.gca().set_title('Graph')
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.tight_layout()
        plt.show()

        time.sleep(0.5)

    #==================================================================#

    def dijkstra_allpaths(self):
        """ Func to repeat the main shortest path finder function to reach all possible ends of the graph from the source node """
        print("\n=============================\nDijkstra's algorithm")

        start = 'a'
        choice = input("Default source = 'a', change? [Y/N]: ")
        if choice.lower() == 'y':
            while True:  # loop to get valid input
                start = input(f"\nEnter source node {set(self.graph.keys())}: ")
                if (start.isalpha()) and (start.lower() in self.graph.keys()):  # check if alpha and in graph
                    start = start.lower()
                    break
                else:
                    print('Enter valid input from {}\n'.format(list(self.graph.keys())))

        print("\n=============================\n")
        # iterate through each node set as destination (other than starting node)
        for x in tqdm(self.graph.keys() - start, unit='Finding shortest paths'):
            graph = self.graph.copy()
            self.dijkstra_path(graph, x, start)
            print("\n=============================\n")
            time.sleep(0.2)

    def dijkstra_path(self, graph, end, start):
        """ Func to find the shortest path from a specified source and end node """
        tic = time.time()

        # showing the path
        print(f"\nStarting from {start} to {end}")

        s_dist = {}  # constantly updating weight
        prev = {}  # store the path of shortest weight
        unseen = graph  # to make sure every node gets seen while iterating
        path = []  # store end shortest path
        for node in unseen:
            s_dist[node] = float('inf')  # initial value
        s_dist[start] = 0  # start node starting with 0

        # greedy algorithm
        while unseen:  # loop until unseen dict is empty
            min = None
            for node in unseen:
                if min is None:  # base case
                    min = node
                elif s_dist[node] < s_dist[min]:
                    min = node

            for child, weight in graph[min].items():  # checking child nodes
                if weight + s_dist[min] < s_dist[child]:
                    # accumulatively adds weight from start to end node
                    s_dist[child] = weight + s_dist[min]
                    # saves the path of the accumulatively added weight
                    prev[child] = min
            unseen.pop(min)

        curr = end
        while curr != start:  # to read the path from goal to start
            path.insert(0, curr)
            curr = prev[curr]  # keep storing previous nodes in shortest path
        path.insert(0, start)
        print('\nSmallest weight is {}'.format(s_dist[end]))
        time.sleep(0.2)
        print("Path is: {}".format(path))
        time.sleep(0.2)
        toc = time.time()
        print(f"Time taken: {toc - tic:.5f}s")

    #==================================================================#

    def show_results(self):
        """ Func to show all the results for each question """
        self.show_graph()
        self.prim()
        self.kruskal()
        self.dijkstra_allpaths()
        time.sleep(1)
        return '\nAshwin Rajesh Jawalikar, 20190802140\nTo Dr. Saif and Ms. Vijaylaxmi -> Thank you for an awesome semester of coding!'


graph = {'a': {'b': 4, 'h': 8},
         'b': {'a': 4, 'h': 11, 'c': 8},
         'h': {'a': 8, 'b': 11, 'i': 7, 'g': 1},
         'i': {'h': 7, 'g': 6, 'c': 2},
         'g': {'h': 1, 'i': 6, 'f': 2},
         'c': {'b': 8, 'i': 2, 'f': 4, 'd': 7},
         'f': {'g': 2, 'c': 4, 'd': 14, 'e': 10},
         'd': {'c': 7, 'f': 14, 'e': 6},
         'e': {'d': 6, 'f': 10}}
lab = Graph(graph)
print(lab.show_results())
