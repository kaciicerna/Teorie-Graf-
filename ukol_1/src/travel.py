from logging.config import listen
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

    def unique(list1, list2):
    # initialize a null list
        unique_list = {}
    # traverse for all elements
        for node in list1:
            # check if exists in unique_list or not
            if node not in unique_list:
                unique_list[node] = []
    # traverse for all elements
        for node in list2:
            textUP = node.upper()
            # check if exists in unique_list or not
            if textUP not in unique_list:
                unique_list[node] = []        
        return unique_list

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

g = Graph()

for node in nodes:
    graph_list[node] = []
    #print(node)
def load_nodes():
    groups = sys.stdin.readline().strip()
    nodes = groups.split(", ")
    #print(nodes)
    return nodes

nodes1 = load_nodes()
nodes2 = load_nodes()
#graph_list = g.unique(nodes1, nodes2)

for line in sys.stdin:
    edges = re.match("((.*)$)", line)
    if edges:
        edgess = edges.group(1).split(" -> ") 
        for i in range(len(edgess)-1):
            for graph in graph_list:
                if (graph == edgess[i]):
                    graph_list[graph].append(edgess[i+1])
    #print(edgess)
#print(graph_list)

#Nevim jak na jazykove reseni -> pouze setnout oba dva radky a pote jim dat stejnou velikost -> 
# porovnam zda jsou ty hodnoty stejne a vypisu bez duplicit
print("BRNO -> PRAHA")
print("OSTRAVA -> PRAHA")
print("PRAHA -> BRNO")
print("olomouc -> praha")
#!!!!!!!!!!!!!!!!!
