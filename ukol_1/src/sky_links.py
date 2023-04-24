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

    def normalize():
        for i in graph_list:
            if i not in vystup:
                vystup.append(i)
        graph_list = vystup

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
radek = input()
graph_list = {}
graph_vystup = {}
groups = re.match(r"^City:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
g = Graph()
for node in nodes:
    graph_list[node] = []

for line in sys.stdin:
    edges = re.match("\\w+:\\s(.*)$", line)
    edgess = edges.group(1).split(" -> ")
    for i in range(len(edgess)-1):
        for graph in graph_list:

            # oteruji jestli uz ten nazev neni na te same pozici
            if graph == edgess[i] and not edgess[i+1] in graph_list[graph]:
                graph_list[graph].append(edgess[i+1])
            elif graph == edgess[i]:
            # ukladam do jineho slovniku
                graph_vystup[graph] = (edgess[i+1])
#prochazim si prvky slovniku a vypisuji vstupy
for vstup in graph_vystup:
    print(f"{vstup} -> {graph_vystup[vstup]}")
