import sys
import re
#4b) rozdeleni do skupin (maly pocet skupin - lidi kteri se neznaji) ->
# barveni grafu . uzlu ->NP uplne problemy

nodes = []
edgess = []
radek = input()
graph_list = {}

groups = re.match(r"(.*)$", radek)
nodes = groups.group(1).split(", ")

for node in nodes:
    graph_list[node] = []

for line in sys.stdin:
    edges = re.match(r"((.*)$)", line)
    if edges:
        edgess = edges.group(1).split(" - ")
        for graph in graph_list:
            if (edgess[0] == graph):
                #odstraneni duplicitnich hodnot
                graph_list[edgess[0]].append(edgess[1])
                graph_list[edgess[1]].append(edgess[0])  
def Color(vertices): 
    result = 0
    if (vertices % 2 == 0):
        result = 2
    else:
        result = 4
    return result
    
if (int(len(graph_list))-Color(int(len(graph_list)))) == 4:
    print("neni mozne")
else:        
    print("Number of all partners in teambuilding:",int(len(graph_list)))
    print ("Number of colors require is:",(int(len(graph_list))-Color(int(len(graph_list)))))
