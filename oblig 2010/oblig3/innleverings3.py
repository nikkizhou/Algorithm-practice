
from typing import Deque
from collections import deque
from collections import defaultdict
from heapq import heappush, heappop

allMovies,allActors = dict(),dict()
#allMovies {'tt8093700':['Ant-Man', 8.3], 'tt8093701': ['Iron Man', 5.7]}
#allActors {'nm0886638': ['Tome', ['tt0051407','tt0051407'], 'nm0886638': ['Mamie', ['tt0063790', 'tt0062514']]}
#E {a1:{a2,a3,a6}, a2:{a1,a4,a6},...} 
#w {(a1,a2): m1, (a1,a3): m2}

def readFileAndBuildGraph():
  w,E = defaultdict(set),defaultdict(set)
  #w: {(a1,a2): {'tt1894616'}, (a2,a3):{'tt0051407','tt0063790'...}}

  with open('input/movies.tsv', encoding='utf8') as f:
    for line in f:
      listt = line.strip().split("\t") #[tt7860140	Nakshatram	3.5	172]
      id,name,score = listt[0],listt[1],float(listt[2])
      allMovies[id]= [name,score]
      
  with open('input/actors.tsv', encoding='utf8') as f:
    movie_actors = defaultdict(set) #{'movie1': {'a1','a2','a3'..}, 'movie2': {'a3', 'a5'}...}
    for line in f:
      listt = line.strip().split("\t") #['nm0886638', 'Mamie Van Doren', 'movie1', 'movie2', 'movie3']
      id,name,movies = listt[0],listt[1],listt[2:]
      allActors[id]= [name, movies]
      #for every movie of each actor, check if there is any other actor that has a common movie
      #if yes, add an edge of these two actors to G
      buildGraph(id,movies,movie_actors,w,E)
  return w,E
    
def buildGraph(actorId,movies, movie_actors,w,E):
  for m in movies:
    if m in allMovies: 
      if movie_actors[m]:  
        for otherActor in movie_actors[m]:
          E[actorId].add(otherActor)
          E[otherActor].add(actorId)
          w[(actorId, otherActor)].add(m)
      movie_actors[m].add(actorId)  

def count(G):
  w,E=G
  edges =0
  for tuple in w:
    edges+=len(w[tuple])
  print(f'- Oppgave 1:\n\nNodes: {len(allActors)} \nEdges: {edges}')
 
#-----------------------------OPPGAVE 2 ------------------------------

def BFSVisit(E,start,end):
  visited,queue  =[],[[start]] #queue is a list of path, path is a list of node/actorId
  while queue:
    path = queue.pop(0) #[{movie1: actor4,},{movie3: acotr2}]
    node = path[-1] #{movie2: actor2}
    if node not in visited:
      visited.append(node)
      for nabo in E[node]:
        newPath = list(path)
        newPath.append(nabo)
        queue.append(newPath)
        if nabo==end:
          return newPath
  print ('\nPath does not exists!')


def finnKortestSti(G,actorId1,actorId2):
  w,E=G
  path = BFSVisit(E,actorId1,actorId2) #['nm0000313', 'nm0000168', 'nm0000458']
  if path is not None:
    print('\n'+allActors[path[0]][0])
    for i in range(1,len(path)):
      actorName=  allActors[path[i]][0]
      movieNames =  w[(path[i-1], path[i])] or w[(path[i], path[i-1])]
      movieId = list(movieNames)[0]
      edge = f'{allMovies[movieId][0]} ({allMovies[movieId][1]})'
      print(f'===[{edge}] ===> {actorName}')

#-----------------------------OPPGAVE 3 ------------------------------
def dijkstra(G, start,end):
  w,E=G
  queue=[(0, start)]
  movie_weight = defaultdict(lambda: float('inf'))  # {start:0, 'actor2':1}
  movie_weight[start]=0
  path = {start: None} #path: {'nm0000313': None, 'nm0005024': ('nm0000313', 'tt0371746'), ...}
  
  while queue:
    nodeWeight,node= heappop(queue)
    if node==end:
      break
    for nabo in E[node]:
      edges = w[(node,nabo)] or w[(nabo,node)]
      maxScore,maxScoreMovieId = getMaxScore(edges)
      c = nodeWeight+(10-maxScore)
      if c < movie_weight[nabo]:
        movie_weight[nabo] = c
        heappush(queue, (c,nabo))
        path[nabo] = (node, maxScoreMovieId)
  return path

def getMaxScore(edges):
  maxScore,maxScoreId =0,None
  for movieId in edges:
    score = allMovies[movieId][1]
    if score > maxScore:
      maxScore,maxScoreId = score,movieId
  return maxScore, maxScoreId

def finnChillestSti(G, start,end):
    w, E = G
    path = dijkstra(G,start,end)
    current, pathList = path[end], []
  
    while current and current[0] in path:
      actorId = current[0]
      pathList.append(current)
      current = path[actorId]
    
    str, totalWeight='',0
    for tuple in reversed(pathList):
      actor = '\n'+allActors[tuple[0]][0]
      weight = allMovies[tuple[1]][1]
      movie = f'{allMovies[tuple[1]][0]} ({weight}) '
      totalWeight += 10-weight
      str += f'{actor}\n===[{movie}] ===>'
    print(f'{str+allActors[end][0]} \nTotal Weight:{totalWeight}')

#-----------------------------OPPGAVE 4 ------------------------------

def DFSvisit(E,node):
  stack, visited= [node],set()
  while stack:
    u=stack.pop()
    if u not in visited:
      visited.add(u)
      for nabo in E[u]:
        stack.append(nabo)
  return visited

def komponenter(G):
  result,visitedTotal = {}, set()
  result = defaultdict(lambda:0,result)
  _,E = G
  for node in E:
    if node not in visitedTotal:
      visitedComps = DFSvisit(E,node)
      visitedTotal = visitedTotal.union(visitedComps)
      result[len(visitedComps)] +=1

  result[1] =len(allActors)-len(E)
  for size in sorted(result):
    print(f'There are {result[size]} components of size {size}')

def main():
  G=readFileAndBuildGraph()
  count(G)

  print('\n- Oppgave 2:')
  finnKortestSti(G,'nm2255973','nm0000460')
  finnKortestSti(G,'nm0424060','nm0000243')
  finnKortestSti(G,'nm4689420','nm0000365')
  finnKortestSti(G,'nm0000288','nm0001401')
  finnKortestSti(G,'nm0031483','nm0931324')

  print('\n- Oppgave 3:')
  finnChillestSti(G,'nm2255973','nm0000460')
  finnChillestSti(G,'nm0424060','nm0000243')
  finnChillestSti(G,'nm4689420','nm0000365')
  finnChillestSti(G,'nm0000288','nm0001401')
  finnChillestSti(G,'nm0031483','nm0931324')
  
  print('\n- Oppgave 4:\n')
  komponenter(G)

main()
