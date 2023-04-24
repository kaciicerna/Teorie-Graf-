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
groups = re.match(r"^Employ:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
g = Graph()
seen = set()

for node in nodes:
    graph_list[node] = []

vystup = []

for line in sys.stdin:
    edges = re.match("\\w+:\\s(.*)$", line)
    if edges:
        edgess = edges.group(1).split(", ") 
        for graph in graph_list:
            #musim zjistit poradi daneho uzlu, zda je na pozici i+1 a nebo je na pozici i-1 od daneho uzlu
            #musim projit oba dva smery, abych si zjistila vsechny uzly s nimiz ma nejaky vztah 
            #pote si ho pridam do grafu ke konkretnimu uzlu s nimz sousedi
            for i in range(0,len(edgess)-1):
                if graph in edgess and edgess[i+1] not in graph_list[graph]:
                    graph_list[graph].append(edgess[i+1])
            for i in range(len(edgess)-1,0,-1):
                if graph in edgess and edgess[i-1] not in graph_list[graph]:
                    graph_list[graph].append(edgess[i-1])
        #print(graph_list)
#Smazou se vsechny duplicitni hodnoty (StuckOverF.)
delete_duplicate = {key:[i for i in value if key != i] for key,value in graph_list.items()}

count = { key: len(value) for key, 
        value in graph_list.items() 
        }
#for input in sorted(count, key=count.get, reverse=True):
            #print (f"{input} ({count[input]})")
if count == max(count):
    #(n*(n-1))/2
    print("True")
else:
    print("Goal: False")

#!!!!!!!!!!!!!!!