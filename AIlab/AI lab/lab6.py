#Lab 7 Python program to implement A* Search
def calcpathcost(path):
  pathcost=0
  for i in range (1,len(path)):
    edge=path[i-1]+path[i]
    stepcost=cost[edge]
    pathcost=pathcost+stepcost
  return pathcost

def AStar():
  expanded = []
  pathq=[start]
  fringe=[start]
  f=h[start]
  fn=[f]
  while fringe:
    m=min(fn)
    mi=fn.index(m)
    node = fringe.pop(mi)
    fn.pop(mi)
    path=pathq.pop(mi)
    if(node==goal):
      print("Goal Found!!!!!")
      print("Solution Path:",path)
      pathcost= calcpathcost(path)
      print("Path Cost:",pathcost)
      break
    else:
      neighbours = graph[node]
      for n in neighbours:
        fringe.append(n)
        new_path=list(path)
        new_path.append(n)
        pathq.append(new_path)
        gn=calcpathcost(new_path)
        fn.append(h[n]+gn)
    expanded.append(node)

graph={'a':['b','c'],'b':['c','d','e'],'c':['d','e'],'d':['g'],'e':['d','g']}
cost={'ab':5,'ac':2,'bc':6,'bd':2,'be':8,'cd':7,'ce':6,'dg':6,'ed':5,'eg':4}
h={'a':9,'b':6,'c':8,'d':4,'e':4,'g':0}
start='a'
goal='g'
AStar()
