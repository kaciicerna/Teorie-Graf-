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
graph_list_one = {}
graph_list_two = {}
oposit_rows_one = {}
oposit_rows_two = {}

groups = re.match(r"^Employ:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
g = Graph()
seen = set()

for node in nodes:
    graph_list_one[node] = []
    graph_list_two[node] = []
    oposit_rows_one[node] = []
    oposit_rows_two[node] = []

for line in sys.stdin:
    edges = re.match("((.*)$)", line)
    if edges:
            edgess = edges.group(1).split(" -> ")
            g.graphNodes
            for graphOne in (graph_list_one):
                if set(graphOne): 
                    if (edgess[0] == graphOne):
                        graph_list_one[edgess[1]].append(edgess[1])
            for graphTwo in (graph_list_two):
                if set(graphTwo): 
                    if (edgess[1] == graphTwo):
                        graph_list_two[edgess[0]].append(edgess[0])
            
            #print(edgess)
print(graph_list_one)
print(graph_list_two)
delete_duplicate_one = {key:[i for i in value if key != i] for key,value in graph_list_one.items()}
delete_duplicate_two = {key:[i for i in value if key != i] for key,value in graph_list_two.items()}

countimport = { key: len(value) for key, 
        value in graph_list_two.items() 
        }
countexport = { key: len(value) for key, 
        value in graph_list_one.items() 
        }

for input in sorted(countimport, key=countimport.get, reverse=True):
            print (f"{input} ({countimport[input]})")
print("................")
for input in sorted(countexport, key=countexport.get, reverse=True):
            print (f"{input} ({countexport[input]})")
#!!!!!!!!!!!!!!!! 