from typing import Deque
from collections import deque
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(G,start, end):
    w,E=G
    queue = [(0, start)]
    movie_weight = defaultdict(lambda: float('inf'))
    movie_weight[start] = 0
    path = {start: []}

    while queue:
        nodeWeight, node = heappop(queue)
        
        if nodeWeight >= movie_weight[end]:
            break
        
        for nabo in E[node]:
            c = nodeWeight + node.best_movie(nabo).weight
            if c < movie_weight[nabo]:
                movie_weight[nabo] = c
                heappush(queue, (c, nabo))
                path[nabo] = path[node] + [node]

    return path[end] + [end], movie_weight[end]


