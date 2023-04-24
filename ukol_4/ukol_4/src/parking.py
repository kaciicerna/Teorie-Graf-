#4c) Manhaticka vzdalenost (mrizka) -> BO - budovy, PO - parkovaci mista, 
# musim spocitat cestu/vzdalenost, aby to bylo nejkratsi od domu k parkovani (parovani)
import sys
import re

nodes = []
edgess = []
graph_list = []
parking_list = {}
building_list = {}
vystup = [] 

def min_Manhatton_distance(b1,b2,p1,p2):
    return (abs((b1-p1)+abs(b2-p2)))

for line in sys.stdin:
        line = line.strip()
        listExit = line.split(' ')
        listExit[1] = listExit[1].replace(':', '')
        listExit1 = listExit.pop(1)
        listExit1 = listExit1.split(',')    
        listExit.insert(1, listExit1[0])
        listExit.insert(2, listExit1[1])
            #print(listExit)
        node1 = listExit[0]
        if not node1 in graph_list:
            graph_list.append(node1)
        vystup.append(listExit)
        if listExit[0][0] == 'B':
            building_list[listExit[0]] = []
            building_list[listExit[0]].append((int(listExit[1]),int(listExit[2]),int(listExit[3])))
        else:
            parking_list[listExit[0]] = []
            parking_list[listExit[0]].append((int(listExit[1]),int(listExit[2]),int(listExit[3])))

        #print(listExit)
#pocatecni uzly
#print(graph_list)

distance = 0
for xp, yp in parking_list.copy().items():
    counter = 1
    max_capacity_parking = yp[0][2]
    for xb, yb in building_list.copy().items():
        max_capacity_building = yb[0][2]
        while max_capacity_building > 0 and max_capacity_parking > 0:
            find_distance = min_Manhatton_distance(yp[0][0], yp[0][1], yb[0][0], yb[0][1])
            vystup.append(f"{xb}_{counter} -> {xp}_{counter}: {find_distance}")
            max_capacity_building -= 1
            max_capacity_parking -= 1
            distance += find_distance
            counter += 1
            if max_capacity_building == 0:
                del building_list[xb]
for vysledek in vystup:
    print(vysledek)
print(f"Celkem: ", distance)

