def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)  #[start]
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)  #[start]
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return
 
# Driver Code

     
# Graph using dictionaries
graph = {'A': ['B', 'E', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']}
  
# Function Call
BFS_SP(graph, 'A', 'D')




if node not in visited:
  naboer = set(sum(graph[node].values(), [])) #graph[s].values(): [[A1,A2,A3],[A1,A4]]  naboer:{A2,A3,A4}
  for nabo in naboer:
    newPath = list(path)
    newPath.append(nabo)
    queue.append(newPath)

     
        """
