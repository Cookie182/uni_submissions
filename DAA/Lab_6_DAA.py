from queue import Queue
import numpy as np
import time

# the given graph (adjacency list format)
tree = {1: [2, 3],
        2: [1, 4],
        4: [2, 3],
        3: [1, 4, 5],
        5: [3, 6],
        6: [5]}

#===================================================================================================#


class Graph:
    def __init__(self, tree, start):
        self.tree = tree
        self.start = start

    def show(self):  # to show the tree and starting node
        start = self.start

        print(f'Start at: {start}')
        for keys, values in tree.items():
            print('Parent: {0}, Values = {1}'.format(keys, values))

    # Breadth first search

    def bfs(self):
        tree = self.tree
        start = self.start

        visited = {}  # store nodes already visited
        trav_turn = {}  # store turns for pre and post visiting
        travel = []  # in order traversal
        queue = Queue()

        for node in tree.keys():
            visited[node] = False  # by default, none are visited
            # print(visited)

        # starting with the source node
        visited[start] = True
        queue.put(start)
        while not queue.empty():
            first_q = queue.get()  # popping left-most element of queue
            travel.append(first_q)

            # to explore the adjacent ver
            for vertex in tree[first_q]:
                if not visited[vertex]:  # checking if vertex not already visited
                    visited[vertex] = True
                    queue.put(vertex)

        print('BFS')
        print('Inorder traversal (BFS) with starting point {} ='.format(
            start), *travel, '\n')
        if set(tree.keys()) == set(travel):  # check if the graph is connected
            print('The tree is connected')
        else:
            print('The tree is not connected')

    #===================================================================================================#

    # Depth first search

    def dfs(self):
        start = self.start
        tree = self.tree

        global trav_turn
        trav_turn = {}  # to store the pre and print visited turn count

        global visited
        visited = {}  # to store already visited nodes

        global travel
        travel = []  # in order traversal

        for node in tree.keys():  # starting values for each node
            visited[node] = False
            trav_turn[node] = [np.nan, np.nan]

        global end_turn  # post visit count
        end_turn = 1

        global start_turn  # pre visit count
        start_turn = 0

        def _dfs(x):  # helper
            global end_turn

            global start_turn
            start_turn += 1

            # starting point
            visited[x] = True
            trav_turn[x][0] = start_turn
            trav_turn[x][1] = end_turn
            travel.append(x)

            # recursively calls the function until it reaches the last node of the parent node
            for y in tree[x]:
                if visited[y] == False:
                    _dfs(y)

            # updating turn counter
            trav_turn[x][1] = start_turn + end_turn
            end_turn += 1
        _dfs(start)

        print('DFS')
        print('Inorder traversal (DFS) with starting point {} ='.format(start), *travel)
        if set(tree.keys()) == set(travel):  # print the counts after checking if graph is connected
            print('The tree is connected')
            print('\nPre and post visited counts:')
            for key, values in trav_turn.items():
                print(f'For node {key}, pre visited count = {values[0]} and post visited count = {values[1]}')
        else:
            print('The tree is not connected')


test = Graph(tree, 1)
test.show()
print('\n#=============================================================#\n')
time.sleep(1)
test.bfs()
print('\n#=============================================================#\n')
time.sleep(1)
test.dfs()
print('\n#=============================================================#\n')
