#3b) projit vsechny hrany, projit prave jednou, nemusi existovat
# euleruv tah
import sys
from collections import defaultdict
graph=defaultdict(list)
def sub(visited, _cur, graph):
    if not graph:
        return visited + [_cur]

    for i, edge in enumerate(graph):
        cur, nex = edge
        if _cur not in edge:
            continue
        _graph = graph[:]
        del _graph[i]
        if _cur == cur:
            res = sub(visited + [cur], nex, _graph)
        else:
            res = sub(visited + [nex], cur, _graph)
        if res:
            return res

def find_eulerian_tour(graph):
    head, tail = graph[0], graph[1:]
    prev, nex = head
    return sub([prev], nex, tail)

nodes = []
edgess = []
graph_list1 = []
graph_list2 = []
graph_list3 = []
vystup = [] 

for line in sys.stdin:
        line = line.strip()
        listExit = line.split(' ')
        listExit = (listExit[0],listExit[1].replace('-|',""),listExit[2])
        node1 = (listExit[0], listExit[2])
        node2 = listExit[2]
        edges = listExit[1].replace('-|',"")
        edges = listExit[1].replace('|-',"")
        if not node1 in graph_list1:
            graph_list1.append(node1)
        if not node2 in graph_list2:
            graph_list2.append(node2)
        if not edges in graph_list3:
            graph_list3.append(edges)
        vystup.append(listExit[1])
#print(graph_list1)
#print(graph_list2)
#print(graph_list3)

print(find_eulerian_tour(graph_list1))
print(("-".join(vystup))+('-|'))