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
graph_list_export = {}
graph_list_import = {}
groups = re.match(r"^Store:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
g = Graph()

for node in nodes:
    graph_list_export[node] = []
    graph_list_import[node] = []

for line in sys.stdin:
    edges = re.match("\\w+:\\s(.*)$", line)
    if edges:
        edgess = edges.group(1).split(" -> ")
        g.graphNodes
        #prochazim si graf uzel po uzlu ve sloupci [0] a priradim to same i sloupec [1]
        for graphExport in (graph_list_export):
            if (edgess[0] == graphExport):
                graph_list_export[edgess[0]].append(edgess[0]) 
        for graphImport in (graph_list_import):
            if (edgess[1] == graphImport):
                graph_list_import[edgess[1]].append(edgess[1]) 

#po pridani uzlu si spocitam jejich pocet a vypisu si maximalni pocet prvniho clena v konkretnim sloupci
countimport = { key: len(value) for key, 
        value in graph_list_export.items() 
        }
countexport = { key: len(value) for key, 
        value in graph_list_import.items() 
        }

for input in sorted(countimport, key=countimport.get, reverse=True)[0:1]:
            print (f"Export: {input} ({countimport[input]})")
for input in sorted(countexport, key=countexport.get, reverse=True)[0:1]:
            print (f"Import: {input} ({countexport[input]})")
