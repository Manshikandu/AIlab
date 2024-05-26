#lab 4.2 write a program to implement IDS in the given graph

import sys

def calcpathcost(path):
    pathcost = 0
    for i in range(1, len(path)):
        edge = path[i-1] + path[i]
        stepcost = cost[edge]
        pathcost += stepcost
    return pathcost

def IDS():
    for depth_limit in range(sys.maxsize):
        fringe = [start]
        pathq = [[start]]
        while fringe:
            node = fringe.pop(0)
            path = pathq.pop(0)
            if node == goal:
                print("Goal Found!!!!!") 
                print("Solution Path:", path)
                pathcost = calcpathcost(path)
                print("Path Cost:", pathcost)
                sys.exit("Good Bye")    
            else:
                neighbours = graph.get(node, [])
                for n in neighbours:
                    level = len(path)
                    if level < depth_limit: 
                        fringe.append(n)
                        new_path = list(path)          
                        new_path.append(n)
                        pathq.append(new_path)

graph = {'a': ['b','c'], 'b': ['c','d','e'], 'c': ['d','e'], 'd': ['g'], 'e': ['d','g']}
cost = {'ab': 5, 'ac': 2, 'bc': 6, 'bd': 2, 'be': 8, 'cd': 7, 'ce': 6, 'dg': 6, 'ed': 5, 'eg': 4}
start = 'a'
goal = 'g'                                                                                                            

IDS()