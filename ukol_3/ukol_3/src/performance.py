# 3a) projit vsechny uzly, za nejkratsi dobu a vratit se do puvodniho uzlu
    # hledani nejkratsi cesty (obchodni cestujici
from itertools import count
import sys
import re
from collections import defaultdict
from heapq import *

def dijkstra(f, t, edges):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, [])], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = [v1]
            if v1 == t:
                return (f"{str(path)+(': ')}, {str(cost)+('m')}")

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return ([], float("inf"))

nodes = []
edgess = []
graph_list = []

vystup = [] 
for line in sys.stdin:
        line = line.strip()
        listExit = line.split(' ')
        listExit = (listExit[0], listExit[2].replace(':', ""), int(listExit[3].replace('m', "")))
        node1 = listExit[0]
        if not node1 in graph_list:
            graph_list.append(node1)
        vystup.append(listExit)

#print(graph_list)

#print(vystup)
if __name__ == "__main__":
    for nodes in graph_list:
        print("".join(dijkstra("A", nodes, vystup)))
