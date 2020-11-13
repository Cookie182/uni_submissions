import numpy as np

graph = {'a': {'b': 5, 'c': 4}, 'b': {'c': 6, 'd': 2}, 'c': {
    'b': 7, 'd': 8, 'e': 2}, 'd': {'e': 8}, 'e': {'d': 9}}


def dijkstra(graph):
    print('Graph:')
    for key, values in graph.items():
        print(key, values)

    while True:
        keys = graph.keys()
        start = input('Starting point from {}: '.format(graph.keys())).lower()
        end = input('End point from {}: '.format(graph.keys() - start)).lower()
        if (start in keys) and (end in keys):
            break
        else:
            print('\nEnter valid keys from graph!')
            continue

    print("\nShowing path from {} to {}".format(start, end))
    s_dist = {}
    prev = {}
    unseen = graph
    path = []
    for node in unseen:
        s_dist[node] = np.inf
    s_dist[start] = 0

    while unseen:
        min = None
        for node in unseen:
            if min is None:
                min = node
            elif s_dist[node] < s_dist[min]:
                min = node

        for child, weight in graph[min].items():
            if weight + s_dist[min] < s_dist[child]:
                s_dist[child] = weight + s_dist[min]
                prev[child] = min
        unseen.pop(min)

    curr = end
    while curr != start:
        try:
            path.insert(0, curr)
            curr = prev[curr]
        except KeyError:
            print('\nPath not reachable')
            break
    path.insert(0, start)
    if s_dist[end] != np.inf:
        print('\nShortest distance is {}'.format(s_dist[end]))
        print("Path is: {}".format(path))


dijkstra(graph)
