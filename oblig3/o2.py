from collections import deque
from collections import defaultdict
import csv
from typing import Deque
from heapq import heappush, heappop

class Actor:
    def __init__(self, name, nm_id):
        self.nm_id = nm_id
        self.name = name
        self.movies = set()
        self.edges = dict()


    def add_movie(self, movie):
        self.movies.add(movie)

    def get_movies(self):
        return self.movies


class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.actors_in_movie = set()

    def add_actor(self, actor):
        self.actors_in_movie.add(actor)

    def get_actors(self):
        return self.actors_in_movie

    def get_rating(self):
        return self.rating

def find_actor(id):
    return actors[id]



def read_files():

    actors_tsv = open('marvel_actors.tsv', encoding='utf-8').read()
    movies_tsv = open('marvel_movies.tsv', encoding='utf-8').read()

    actors = dict()
    movies = dict()

    # leser inn fra fil over filmer, og lager film-objekter
    for line in movies_tsv.splitlines():
        id, title, rating, _ = line.split('\t')
        movies[id] = Movie(title, rating)

    # leser inn fra fil over skuespillere, og lager skuespiller-objekter
    for actor in actors_tsv.splitlines():
        id, name, *actor_movies = actor.split('\t')
        actors[id] = Actor(name, id)

        # Legger til skuespillere i filmobjectet tilhørende film de spiller i.
        # Dersom filmen ikke finnes, tar vi den ikke med.
        for movie in actor_movies:
            if movie in movies:
                actors[id].add_movie(movie)
                movies[movie].add_actor(id)

    return actors, movies

def count(G):
    actors, movies = G
    nodes = len(actors)
    edges = 0

    for movie in movies:
        actors_movie = movies[movie].actors_in_movie
        # tar N*(N-1)/2, der N= antall noder, for å finne antall kanter
        edges += int(len(actors_movie)*(len(actors_movie)-1)/2)

    return "antall noder:" + str(nodes) + " antall kanter:"+ str(edges)

#trenger kun til å tegne grafen?
def set_edges():
    for a in actors.values():
        for m in a.movies:
            movie = movies[m]
            for co_actor in movie.actors_in_movie:
                if co_actor != a:
                    a.edges[co_actor] = movie

def build_graph():
    V = set()
    E = defaultdict(set)
    w = dict()

    for v in actors:
        for u in v.edges.keys():
            V.add(v)
            V.add(u)

            E[v].add(u)
            #E[u].add(v)

            w[(v,u)]= v.edges.get(u)
            #w[(u,v)]= v.edges.get(u)

    return V, E, w

def draw_graph(G):
    V, E, w = G
    dot = graphviz.Graph()
    seen_edges = set()

    for v in V:
        dot.node(v.nm_id, v.name)

        for u in E[v]:
            if (u,v) in seen_edges:
                continue
            seen_edges.add((v,u))
            dot.edge(v.nm_id, u.nm_id, label=(str((w[(v,u)]).title) + str((w[(v,u)]).rating)))

    dot.render('graph', format='svg')

    dot.render('test-output/test-oppg1.gv', view=True)
    'test-output/test-oppg1.gv.pdf'

def shortest_path_parents(G,start,end=None):
    V, E = G
    parents = {start : (None, None)}
    queue = deque([start])

    while queue:
        # henter ut fra køen, first in first out
        v = deque.popleft(queue)

        # ser først på alle kantene til en node
        for e in V[v].get_movies():
            #Finner alle noder som forbindes med kanten
            for u in E[e].get_actors():

                # finner vi sluttnoden vår så retuneres
                if u == end:
                    parents[u] = (v,e)
                    return parents

                # hvis noden ikke finnes i foreldrene fra før av så legges den
                # til, og settes igjen tilbake i køen
                if u not in parents:
                    parents[u] = (v, e)
                    queue.append(u)

    return parents

def find_shortest_path(G, parents, end):
    v = (end, None)
    path = []

    # for ordensskyld om slutt ikke finnes så
    # returnerer vi den tomme listen
    if end not in parents:
        return path

    while v[0]:
        path.append(v)
        v = parents[v[0]]

    return path[::-1]

def find_chillest_path(G, start, end=None):

    V, E = G #setter actors dictionary til noder, og movies til kanter
    #legger til første steg i køen, dette vil ikke koste oss noe.
    Q = [(0, 0, start)]
    D = defaultdict(lambda: (float('inf'), float('inf'))) #Oppretter en defaultdict D for (Antall steg, rating).

    D[start] = (0,0) #setter steg til start

    parents_path = {start : (None, None)}
    final_step = float('inf')

    while Q:
        step, rating, v = heappop(Q)

        step += 1
        if final_step < step:
            return parents_path

        for e in V[v].get_movies():
            movie_rating = (10-float(E[e].get_rating()))
            total_rating = rating + movie_rating
            # oppdaterer kosten til den aktualle kanten

            # sjekker nodene som den aktuelle kanten leder til
            for u in E[e].get_actors():
                if end == u:
                    final_step = step
                # finner den kanten som koster oss minst
                if step <= D[u][0] and total_rating <= D[u][1] and v != u:
                    D[u] = (step, total_rating)
                    heappush(Q, (step, total_rating, u))
                    parents_path[u] = (v, e)


    return parents_path

def components_and_size(G):
    V, E = G
    comp_size = dict()
    key_V = list(V.keys())

    while key_V:
        start = key_V[0]
        parents = shortest_path_parents(G, start)

        if len(parents) in comp_size:
            comp_size[len(parents)] = comp_size[len(parents)] + 1
        else:
            comp_size[len(parents)] = 1
        key_V = [x for x in key_V if x not in parents]

    return comp_size

def nice_print(G, start, path, weight= False):
    V, E = G
    w = 0

    print()
    print(V[start[0]].name)

    for i in range(len(path)-1):
        # finner rating fra film-objekt i kantene
        rating = E[path[i][1]].rating
        # finner tittel fra film-objekt i kantene
        title = E[path[i][1]].title
        # finner navn på skuespiller fra noder
        next_actor = V[path[i+1][0]].name
        # setter vekt
        w += (10-float(rating))

        print(f'===[ {title} ({rating}) ] ===> {next_actor}')
    if weight:
        print(f'Total weight: {round(w,1)}')

def main():
    print("oppgave 1: ")
    G = read_files()
    print(count(G))

    #tegne grafen:
    #G = build_graph(T)
    #draw_graph(G)

    print(" ")

    print("oppgave 2: ")
    path1 = find_shortest_path(G, shortest_path_parents(G, 'nm2255973'),'nm0000460')
    path2 = find_shortest_path(G, shortest_path_parents(G, 'nm0424060'),'nm0000243')
    path3 = find_shortest_path(G,shortest_path_parents(G, 'nm4689420'),'nm0000365')
    path4 = find_shortest_path(G,shortest_path_parents(G, 'nm0000288'),'nm0001401')
    path5 = find_shortest_path(G,shortest_path_parents(G, 'nm0031483'),'nm0931324')
    nice_print(G, path1[0], path1)
    nice_print(G, path2[0], path2)
    nice_print(G, path3[0], path3)
    nice_print(G, path4[0], path4)
    nice_print(G, path5[0], path5)

    print(" ")

    print("oppgave 3: ")
    path6 = find_shortest_path(G, find_chillest_path(G,'nm2255973'),'nm0000460')
    path7 = find_shortest_path(G, find_chillest_path(G,'nm0424060'),'nm0000243')
    path8 = find_shortest_path(G, find_chillest_path(G,'nm4689420'),'nm0000365')
    path9 = find_shortest_path(G, find_chillest_path(G,'nm0000288'),'nm0001401')
    path10 = find_shortest_path(G, find_chillest_path(G,'nm0031483'),'nm0931324')
    nice_print(G, path6[0], path6, weight=True)
    nice_print(G, path7[0], path7, weight=True)
    nice_print(G, path8[0], path8, weight=True)
    nice_print(G, path9[0], path9, weight=True)
    nice_print(G, path10[0], path10, weight=True)

    print(" ")
    print("oppgave 4: ")
    liste = components_and_size(G)
    for key, val in reversed(sorted(liste.items())):
        print(f'There are {val} components of size {key}')

main()
