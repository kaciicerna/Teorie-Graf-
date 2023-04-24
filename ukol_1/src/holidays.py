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
radek = input()
graph_list = {}
groups = re.match(r"^Places:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
g = Graph()

for node in nodes:
    graph_list[node] = []

for line in sys.stdin:
    edges = re.match("\\d+:\\s(.*)$", line)
    edgess = edges.group(1).split(" -> ")
    for graph in graph_list:
            if (edgess[0] == graph):
                #odstraneni duplicitnich hodnot
                graph_list[edgess[0]].append(edgess[1])
                graph_list[edgess[1]].append(edgess[0])
    #print(edgess)

count = { key: len(value) for key, 
        value in graph_list.items() 
        }
vypis = []
for input in sorted(count, key=count.get, reverse=False):
    if count[input] == 0:
        vypis.append(input)
print(", ".join(vypis))