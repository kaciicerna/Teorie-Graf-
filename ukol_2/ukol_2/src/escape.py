#2c)
    # nejkratsi cesta - ze sekce mustek do unikovy_modul
    # prochazeni grafu (sirka a hloubka) - nezname bludiste
    # vysledky jsou u kazdeho jine, dat si pozor na vysledky (dlouhy vysledek - projit vsechny uzly)

import sys
import re

class Graph: 
    graphNodes = []
    coutner = 0

    def addEdge(self, vstup, vystup, weight=1):
        self.graphNodes.append([vstup, vystup, weight])

    def addNodes(self, node):
        return Graph(
            nodes = self._nodes+[node]
        )

    def printEdgeList(self):
        num_of_edges = len(self.graphNodes)
        for i in range(num_of_edges):
            print("Edge ", i+1, ": ", self.graphNodes[i])

    def countFrequency(graphNodes):
        return Graph.Counter(graphNodes)

class Edge:
    vstup = None
    vystup = None
    def __init__(self, vstup, vystup, weight=1) -> None:
        self.vstup = vstup
        self.vystup = vystup
        self.weight = weight

class Node: 
    name = None
    edged = None
    def __init__(self, name, edges) -> None:
        self.name = name
        if not edges:
            self.__edges = []
        else: self.__edges = edges

nodes = []
edgess = []
inp = input()
graph_list = {}
from_node = []
to_node = []
vystup = []
dijktr = []
groups = re.match(r"^Sections:\s(.*)$", inp)
nodes = groups.group(1).split(", ")
g = Graph()

for node in nodes:
    graph_list[node] = []

for line in sys.stdin:
    edges = re.match(r"((.*)$)", line)
    if edges:
        edgess = edges.group(1).split(" - ")
        from_node.append(edgess[0])
        to_node.append(edgess[1])
        vystup.append(edgess)
#zde je dan pocatecni uzel na nulte pozici, v tomto pripade mustek
start_node = vystup[0][0]
end_node = vystup[6][1]
#porovnam pocatecni uzel, zda se nerovna poslednimu uzlu
while start_node != end_node:
    for random_node in vystup:
        if random_node[0] == start_node:
            dijktr.append(f"{random_node[0]} -> {random_node[1]}")
            start_node = random_node[1]
        elif random_node[1] == start_node:
            dijktr.append(f"{random_node[1]} -> {random_node[0]}")
            start_node = random_node[0]
#vypis minimalni cesty z vystupoveho pole, ktere jsme tam pridali
for vystup_list in dijktr:
   print(vystup_list)
print("")
print("Tady pokud dam na tvrdo unikovy modul tak mi to napise TIME OUT, jinak funguje")