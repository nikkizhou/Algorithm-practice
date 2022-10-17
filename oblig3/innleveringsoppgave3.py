from re import A
from typing import Deque
from collections import deque

class Actor:
  def __init__(self,id,name):
    self.id = id
    self.name = name
    self.movies = list()

  def addMovie(self,actor):
    self.movies.append(actor)
  
  def getMovies(self):
    return self.movies

  def __hash__(self):
     return hash(self.id)
    
  def __eq__(self, other):
    return self.id == other.id
  
  def __repr__(self):
    return self.name

class Movie:
  def __init__(self,id,name,score):
    self.id=id
    self.name = name
    self.score = score
    self.actors = list()

  def addActor(self,actor):
    self.actors.append(actor)

  def getActors(self):
    return self.actors
  
  def __hash__(self):
     return hash((self.id, self.name))
    
  def __eq__(self, other):
        return (self.name, self.id) == (other.name, other.id)

  def __repr__(self):
    return self.name


allMovies = dict() # {'tt8093700':M1, 'tt8093701':M2}
allActors = dict()
graph = {}

def readFile():
  with open('marvel_movies.tsv', encoding='utf8') as f:
    for line in f:
      listt = line.strip().split("\t") #[tt7860140	Nakshatram	3.5	172]
      id,name,score = listt[0],listt[1],listt[2]
      allMovies[id]= Movie(id,name,score)

  with open('marvel_actors.tsv', encoding='utf8') as f:
    for line in f:
      listt = line.strip().split("\t") #['nm0886638', 'Mamie Van Doren', 'tt0051407', 'tt0063790', 'tt0062514']
      id,name,movies = listt[0],listt[1],listt[2:]
      actor = Actor(id,name)
      allActors[id]= actor

      #add the actor to Movie instance
      for m in movies:
        if m in allMovies:
          allMovies[m].addActor(actor)
          actor.addMovie(allMovies[m])
  
def buildGraph():
  #allActors: {'nm2332':A1, 'nm4243':A2}
  for actorObj in allActors.values():
    graph[actorObj]={}
    for movieObj in actorObj.getMovies():
      if movieObj in allMovies.values():
        filtered = filter(lambda actor: actor != actorObj, movieObj.getActors())
        graph[actorObj][movieObj] = list(filtered)
  teller()


def teller():
  antNodes = len(allActors)
  edgesDouble = 0
  for actorObj in graph.values():
    for actorList in actorObj.values():
      edgesDouble+=len(actorList)
  print(f'- Oppgave 1 \nNodes: {antNodes} \nEdges: {int(edgesDouble/2)}')


def findEdge(actor1, actor2):
  for movieObj in graph[actor1]:
    for actorObj in graph[actor1][movieObj]:
      if actorObj == actor2:
        return movieObj
  return (f'No edge between {actor1} and {actor2}')


# s is a actor object
def BFSVisit(start,end):
  start = allActors[start]  #start is a actor object
  end = allActors[end]
  visited =[]
  queue = [[start]] #queue is a list of path, path is a list of node/actor obj
  

  while queue:
    path = queue.pop(0) #[{movieObj: actorObj},{movieObj2: actorObj2}]
    node = path[-1] #{movieObj2: actorObj2}

    if node not in visited:
      naboer = set(sum(graph[node].values(), [])) #graph[s].values(): [[A1,A2,A3],[A1,A4]]  naboer:{A2,A3,A4}
      for nabo in naboer:
        newPath = list(path)
        newPath.append(nabo)
        queue.append(newPath)

        if nabo==end:
          return newPath

    visited.append(node)
  
  print ('\n- Oppgave 2 \nPath does not exists!')

def FinnKortestSti(actorId1,actorId2):
  path = BFSVisit(actorId1,actorId2)
  if path is not None:
    print(f'\n- Oppgave 2 \n{path[0]}')
    for i in range(1,len(path)):
      kant = findEdge(path[i-1],path[i]) 
      print(f'===[{kant} ] ===> {path[i]}')
  

readFile()
buildGraph()
FinnKortestSti('nm0000313','nm0000458')

"""
graph = {
  A1: {M1: [A2,A3], M2:[A4] },
  A2: {M1: [A1], M3:[A7] },
}
"""
