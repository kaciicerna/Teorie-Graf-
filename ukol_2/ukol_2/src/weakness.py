#2b)
#To jsem bohuzel nestihla udelat

import sys
import re
import math  

# def find_bridges(adj_list):
#     dfs_counter = 0
#     n = len(adj_list) 
#     dfs_ord = [math.inf] * n
#     low_link = [math.inf] * n
#     visited_vertices = [None] * n
#     parent_vertex = [-1] * n
#     for i in range(n):
#         if visited_vertices[i] == False:
#             dfs(i, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list)
# def dfs(u, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list):
#     visited_vertices[u] = True
#     dfs_ord[u] = dfs_counter
#     low_link[u] = dfs_counter
#     dfs_counter += 1
#     for v in adj_list[u]:
#         if visited_vertices[v] == "Zadna":
#             parent_vertex[v] = u
#             dfs(v, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, adj_list)
#             low_link[u] = min(low_link[u], low_link[v])
#             if low_link[v] > dfs_ord[u]:
#                 print(" " + (u) + " " + (v) + " ")
#         elif v!= parent_vertex[u]:
#             low_link[u] = min(low_link[u], dfs_ord[v])

nodes = []
edgess = []
radek = input()
graph_list = {}
graph_vystup = {}
vystup = []
groups = re.match(r"^City:\s(.*)$", radek)
nodes = groups.group(1).split(", ")
for node in nodes:
    graph_list[node] = []

for line in sys.stdin:
    edges = re.match("\\w+:\\s(.*)$", line)
    edgess = edges.group(1).split(" -> ")
    for i in range(len(edgess)-1):
        for graph in graph_list:
            for i in range(0,len(edgess)-1):
                if graph in edgess and edgess[i+1] not in graph_list[graph]:
                    graph_list[graph].append(edgess[i+1])
            for i in range(len(edgess)-1,0,-1):
                if graph in edgess and edgess[i-1] not in graph_list[graph]:
                    graph_list[graph].append(edgess[i-1])
#print(graph_list)
# print("-------------------")
# print("Bridges: ")
# print(find_bridges(vystup))
count = { key: len(value) for key, 
        value in graph_list.items() 
        }
for input in sorted(count, key=count.get, reverse=True)[0:2]:
    if count[input]-1 == 3 and 4:
        vystup.append(input)
    else:
        print("Zadna")
print(" -> ".join(vystup))
