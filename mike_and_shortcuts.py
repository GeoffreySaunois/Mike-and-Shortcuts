from typing import List, Dict, Set
from heapq import *
import sys

input_ = sys.stdin.readline
MAX_VAL = 1e10


def read_int() -> int:
    return int(input_())


def read_list() -> List[int]:
    return list(map(int, input_().split()))


# Dijkstra algorithm O(n*log(n))
def dijkstra(n: int, graph: Dict[int, Set[int]]) -> List[int]:
    dist = [0 if not i else MAX_VAL for i in range(n)]
    queue = [(dist[i], i) for i in range(n)]
    heapify(queue)
    seens = set()
    while queue:
        while queue and queue[0][1] in seens:
            heappop(queue)
        if not queue:
            break
        _, u = heappop(queue)
        seens.add(u)
        for v in graph[u]:
            if v not in seens:
                new_dist = dist[u] + 1
                dist[v] = min(dist[v], new_dist)
                heappush(queue, (new_dist, v))
    return dist


def compute_energy(n: int, shortcuts: List[int]) -> List[int]:
    # Edge case
    if n == 1:
        return [0]

    # Setting up the graph structure
    graph = {x: {x-1, x+1} for x in range(1, n-1)}
    graph[0] = {1}
    graph[n-1] = {n-2}

    # Adding shortcuts
    for x, y in enumerate(shortcuts):
        if x != y-1:
            graph[x].add(y-1)

    # Computing minimum energy to reach each intersection
    res = dijkstra(n, graph)
    return res


def process() -> None:
    n = read_int()
    shortcuts = read_list()
    res = compute_energy(n, shortcuts)
    print(*res)


if __name__ == '__main__':
    process()
