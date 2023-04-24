import sys
import re
import heapq
#Dijkstruv algoritmus minimalni cesty
""" def dijkstra(graph, src):
    dist = {vertex: float('inf') for vertex in graph}
    dist[src] = 0

    pq = [(0, src)]
    while len(pq) > 0:
        cur_dist, cur_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if cur_dist > dist[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex].items():
            distance = cur_dist + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist """
nodes = []
edgess = []
radek = input()
vystup = []
neighbor = []
visited_nodes = []
shortest_path = []

for line in sys.stdin:
    edges = re.match(r"((.*)$)", line)
    if edges:
        edgess = edges.group(1)
        list = re.split(r'[-:]', edgess)
        list = [x.strip(' s') for x in list]
        list = (list[0], list[1], int(list[2]))
        vystup.append(list)
#sorted vystup by times line
vystup = sorted(vystup, key=lambda x: x[2])

for steps in vystup:
    neighbor.append(steps[0:2])
first_node = neighbor[0][0]
visited_nodes.append(first_node)
for steps in neighbor:
    if steps[0] not in visited_nodes or steps[1] not in visited_nodes:
        visited_nodes.append(steps[0])
        visited_nodes.append(steps[1])
        shortest_path.append(f"{steps[0]} - {steps[1]}")


for short_path in shortest_path:
    print(short_path)
#print(vystup)
#print(dijkstra(vystup, 'motory'))

