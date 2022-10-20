from collections import defaultdict
from heapq import heappush, heappop
from collections import deque
from typing import DefaultDict

# Bygger grafen som er inspirert fra Lars sin implementasjon i forelesningsnotatet


def buildgraph():

    V = set()
    E = defaultdict(set)
    w = defaultdict(list)

    # Kant skal bestaa av to skuespillere som er bundet til en film
    # ActorToMovies er hashmap hvor "id-name" er nøkkel og "filmene" er verdier,
    # idToName er ogsaa hashmap hvor "id-name" er nøkkel og "navnet" er skuespillernavnet
    actorToMovies, idToName = readFromFileActors()

    movieIdToName, movieRating = readFromFileMovies()

    movieActors = defaultdict(list)

    # Gaar igjennom alle skuespillere knyttet til en gitt film
    for actor in actorToMovies.keys():
        V.add(actor)
        # Går igjennom alle filmer som en gitt skuespiller finnes i
        for movie in actorToMovies[actor]:
            if not movie in movieRating:  # hvis filmen ikke har noen vekt
                continue
            if movieActors[movie]:  # hvis filmen allerede er i dict
                # lag kanter og vekter mellom alle andre skuspillere
                for otherActor in movieActors[movie]:
                    E[actor].add(otherActor)
                    E[otherActor].add(actor)

                    w[(actor, otherActor)].append(
                        (float(movieRating[movie]), movie)
                    )
                    w[(otherActor, actor)].append(
                        (float(movieRating[movie]), movie)
                    )

            movieActors[movie].append(actor)  # legge til skuspiller til film

    return V, E, w, idToName, movieIdToName, movieRating

# Returnerer antall noder(skuespillere) som finnes i grafen


def antallNoder(G):
    V, E, _, _, _, _ = G
    print(len(E),'test!!')
    return(len(V))

# Returnerer antall kanter(film mellom to skuespillere) som finnes i grafen
# ved aa dele antall vekter paa 2


def antallKanter(G):
    V, _, w, _, _, _ = G
    antallKanter = 0
    for node in w.keys():
        antallKanter += len(w[node]) / 2
    return int(antallKanter)

# Returnerer ordboeker for
# filmidTilNavn(filmid er noekkel, navnet er verdien)
# filmTilRating(filmid er noekkel, rating er verdien)
# fra movies.tsv fil


def readFromFileMovies():
    # tt-id Tittel Rating AntallStemmer
    file = open('movies.tsv', encoding="utf8")  # Filplassering
    movieIdToName = dict()
    movieRating = dict()

    for line in file:
        data = line.strip().split('\t')
        id = data[0]
        tittel = data[1]
        rating = data[2]
        movieRating[id] = rating
        movieIdToName[id] = tittel
        #print('reading movies')

    file.close()

    return movieIdToName, movieRating

# Returnerer ordboeker for
# actorToMovies(skuespillerid er noekkel, filmID er verdien)
# idToName(skuespillerid er noekkel, navnet på skuespilleren er verdien)
# fra actors.tsv fil


def readFromFileActors():
    # nm-id Navn tt-id1 tt-id2 . . . tt-idk
    file = open('actors.tsv', encoding="utf8")  # Filplassering
    actorToMovies = {}
    idToName = {}

    for line in file:
        data = line.strip().split('\t')
        id = data[0]
        name = data[1]
        movies = set()

        for movie in data[2:]:
            movies.add(movie)
            

        actorToMovies[id] = movies
        idToName[id] = name
        #print('reading actors',line)
    file.close()
    return actorToMovies, idToName

# Returnerer dict med foreldre noder med forelder og vekt mellom dem
# korteste vei er basert på vekten, og funnet ved hjelp av Dijkstra-algoritmen


def kortesteVei(G, fra, til):
    _, E, w, _, _, _ = G

    Q = [(0, fra)]
    D = defaultdict(lambda: float('inf'))
    D[fra] = 0
    parents = {fra: None}

    while Q:
        cost, v = heappop(Q)
        if v == til:
            break

        for u in E[v]:
            listeOverFilmer = w[(v, u)]
            # Lager tuppel hvor rating er foerste verdien imens filmid er andre
            minsteTuppel = max(listeOverFilmer)
            minsteVerdi = 10 - minsteTuppel[0]
            minsteId = minsteTuppel[1]
            c = cost + minsteVerdi
            if c < D[u]:
                D[u] = c
                heappush(Q, (c, u))
                parents[u] = (v, minsteId)

    return skrivKortesteVei(G, parents, fra, til)

# Skriver ut korteste vei fra dict parents, og lager utskrivbar strenge fra denne


def skrivKortesteVei(G, parents, fra, til):
    V, E, w, idToName, movieIdToName, movieRating = G
    print(parents,'path')

    current = parents[til]
    print(current,'current')
    listeData = []

    while current and current[0] in parents:
        skuspillerID = current[0]
        listeData.append([current[0], current[1]])
        print(listeData,'listdata')
        current = parents[skuspillerID]
    print(listeData,'listeData etter løk')

    strenge = ""
    listeData.reverse()
    totalvekt = 0
    for linje in listeData:
        skuspillerID = linje[0]
        filmID = linje[1]
        skuespillerNavn = idToName[skuspillerID]
        filmNavn = movieIdToName[filmID]

        strenge += skuespillerNavn + "\n" + \
            "===[" + filmNavn + \
            " ( " + movieRating[filmID] + " ) " + "]" + "===> "
        totalvekt += 10 - float(movieRating[filmID])

    strenge += str(idToName[til] + "\n" +
                   "Total weight: " + ("%.1f" % totalvekt) + "\n")

    return strenge

# Returnerer stien mellom "fra" og "til" i en ordbok


def bfsShortestPath(G, fra, til):
    _, E, w, idToName, movieIdToName, movieRating = G
    parents = {fra: None}
    queue = deque([fra])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        if v == til:
            break
        for neighbor in E[v]:
            if neighbor not in parents:
                listeOverFilmer = w[(v, neighbor)]
                filmratingOgId = listeOverFilmer[0]
                filmId = filmratingOgId[1]
                parents[neighbor] = (v, filmId)
                queue.append(neighbor)

    return parents

# Returnerer strengen som skal skrive korteste vei mellom "fra" og "til"


def shortestPathBetween(G, fra, til):
    parents = bfsShortestPath(G, fra, til)
    current = parents[til]
    path = []
    _, E, w, idToName, movieIdToName, movieRating = G

    if til not in parents:
        return path

    while current and current[0] in parents:
        skuspillerID = current[0]
        path.append([current[0], current[1]])

        current = parents[skuspillerID]

    linjeData = path[::-1]

    strenge = ""
    for linje in linjeData:
        skuspillerID = linje[0]
        filmID = linje[1]
        skuespillerNavn = idToName[skuspillerID]
        filmNavn = movieIdToName[filmID]

        strenge += skuespillerNavn + "\n" + \
            "===[" + filmNavn + \
            " ( " + movieRating[filmID] + " ) " + "]" + "===> "

    strenge += str(idToName[til] + "\n")

    return strenge

# metoden gjoer et dybde forst sok, og gaar igjennom alle skuspillere
# legger alle skuspillere som kan naas fra en node(komponent), i en liste,
# og legger denne i enda en liste
# sjekker saa lengden paa alle lister i listen, og mapper storrelsen paa komponenten
# til antall av storrelsen, og returnerer denne dictionayen


def komponenter(G):
    V, E, _, _, _, _ = G

    # antallAvStorrelse[storrelse] = antall
    antallAvStorrelse = defaultdict(int)

    alleKomponenter = []
    alleVisited = set()

    for s in V:
        if s in alleVisited:
            continue

        visited = set([s])
        stack = [s]
        result = []

        while stack:
            v = stack.pop()
            result.append(v)
            for u in E[v]:
                if u not in visited:
                    visited.add(u)
                    alleVisited.add(u)
                    stack.append(u)
        alleKomponenter.append(result)

    for komponent in alleKomponenter:
        l = len(komponent)
        antallAvStorrelse[l] += 1

    return antallAvStorrelse

# lager en utskrivbar strenge fra dictionary antallAvStorrelse


def utskriftKomponenter(G):

    antallAvStorrelse = komponenter(G)

    dictionary_items = antallAvStorrelse.items()

    sorted_items = sorted(dictionary_items, reverse=True)

    strenge = ""
    for storrelseAntall in sorted_items:
        strenge += f"There are {storrelseAntall[1]} components of size {storrelseAntall[0]} \n"

    return strenge


def main():
    # Oppgave 1
    G = buildgraph()
    print("Oppgave 1: \n")
    print(antallNoder(G))
    print(str(antallKanter(G)) + "\n")

    # Oppgave 2
    print("Oppgave 2: \n")

    # Oppgave 3
    print("Oppgave 3: \n")
    print(kortesteVei(G, 'nm0000313','nm0000458'))

    # oppgave 4
    print("Oppgave 4: \n")
    print(utskriftKomponenter(G))


main()
