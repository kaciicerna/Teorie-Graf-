#4a)první je kapacita, ostatni radky je pruchod lidi za minutu, 
# za jak dlouho se dostanou ven a po jak velikych skupinach, pokud vetsi nez ta skupina oznacim !
#Kudy bude kolik lidi utikat, aby se dostalo ven -> maximalni tok v síti
# Ford-Fulkerson algorith in Python
import sys
import re

class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name
        self.source = source
        self.sink = sink

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.returnEdge = None

class FlowNetwork:
    def __init__(self):
        self.vertices = []
        self.network = {}

    def getSource(self):
        for vertex in self.vertices:
            if vertex.source == True:
                return vertex
        return None

    def getSink(self):
        for vertex in self.vertices:
            if vertex.sink == True:
                return vertex
        return None

    def getVertex(self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex

    def vertexInNetwork(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return True
        return False

    def getEdges(self):
        allEdges = []
        for vertex in self.network:
            for edge in self.network[vertex]:
                allEdges.append(edge)
        return allEdges

    def addVertex(self, name, source=False, sink=False):
        if source == True and sink == True:
            return "Vertex cannot be source and sink"
        if self.vertexInNetwork(name):
            return "Duplicate vertex"
        if source == True:
            if self.getSource() != None:
                return "Source already Exists"
        if sink == True:
            if self.getSink() != None:
                return "Sink already Exists"
        newVertex = Vertex(name, source, sink)
        self.vertices.append(newVertex)
        self.network[newVertex.name] = []

    def addEdge(self, start, end, capacity):
        if start == end:
            return "Cannot have same start and end"
        if self.vertexInNetwork(start) == False:
            return "Start vertex has not been added yet"
        if self.vertexInNetwork(end) == False:
            return "End vertex has not been added yet"
        newEdge = Edge(start, end, capacity)
        returnEdge = Edge(end, start, 0)
        newEdge.returnEdge = returnEdge
        returnEdge.returnEdge = newEdge
        vertex = self.getVertex(start)
        self.network[vertex.name].append(newEdge)
        returnVertex = self.getVertex(end)
        self.network[returnVertex.name].append(returnEdge)

    def getPath(self, start, end, path):
        if start == end:
            return path
        for edge in self.network[start]:
            residualCapacity = edge.capacity - edge.flow
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                result = self.getPath(edge.end, end, path + [(edge, residualCapacity)])
                if result != None:
                    return result

    def calculateMaxFlow(self):
        source = self.getSource()
        sink = self.getSink()
        if source == None or sink == None:
            return "Network does not have source and sink"
        path = self.getPath(source.name, sink.name, [])
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.returnEdge.flow -= flow
            path = self.getPath(source.name, sink.name, [])
        return sum(edge.flow for edge in self.network[source.name])

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            # Adding the path flows
            max_flow += path_flow
            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


radek = input()
graph_list = {}
groups = re.match(r"^M01:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
vystup = [] 
for line in sys.stdin:    
        line = line.strip()
        listExit = line.split(' ')
        listExit = (listExit[1], listExit[3], int(listExit[4]))
        vystup.append(listExit)
#pocatecni uzly
print(vystup)

graph = [[0, 8, 0, 0, 4, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 8, 3],
         [2, 0, 0, 0, 0, 5],
         [0, 0, 8, 4, 0, 0],
         [0, 0, 8, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
fn = FlowNetwork()
fn.addVertex("M01", True, False)
fn.addVertex("M05", False, True)
map(fn.addVertex, ["M02", "M03","MP4"])
fn.addEdge("M01", "M02", 15)
fn.addEdge("M02", "M03", 15)
fn.addEdge("M01", "M03", 25)
fn.addEdge("M03", "M04", 15)
fn.addEdge("M03", "M05", 5)
fn.addEdge("M01", "M04", 15)
fn.addEdge("M04", "M05", 25)


source = 0
sink = 5
print("--------------------")
print("Time: %d " % g.ford_fulkerson(source, sink))
#print("Time: %d " % fn.calculateMaxFlow())
print(["%s -> %s; %s/%s" % (e.start, e.end, e.flow, e.capacity) for e in fn.getEdges()])
print("Bohuzel mi nefunguje posloupny vystup i kdyz ho zadavam")