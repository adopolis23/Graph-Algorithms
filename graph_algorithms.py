



def bfs(graph, start_node, search_node=None):
    # graph: a dictionary representing the graph to be traversed.
    # start_node: a string representing the starting node of the traversal.
    # search_node: an optional string representing the node being searched for in the graph.
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    #The output depends on whether the search_node is provided or not:
        #1. If search_node is provided, the function returns 1 if the node is found during the search and 0 otherwise.
        #2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    #if the node to search for is where we start then no need to search
    if start_node == search_node:
        return 1

    #data structure being used for the search
    queue = []
    queue.append(start_node)
    curr_index = 0 



    while curr_index < len(queue):
        
        for connected_node in graph[queue[curr_index]]:
            if connected_node == search_node:
                return 1

            if connected_node not in queue:
                queue.append(connected_node)

        curr_index = curr_index + 1

    if search_node == None:
        return queue
    


    return 0

    '''
    #Useful code snippets (not necessary but you can use if required)
    if search_node and node == search_node:
        return 1  # search node found

    if search_node is not None:
        return 0  # search node not found
    '''

    #return path  # search node not provided, return entire path [list of nconst values of nodes visited]


















def dfs(graph, start_node, visited=None, path=None, search_node=None):
    # graph: a dictionary representing the graph
    # start_node: the starting node for the search
    # visited: a set of visited nodes (optional, default is None)
    # path: a list of nodes in the current path (optional, default is None)
    # search_node: the node to search for (optional, default is None)

    # Note1: The optional parameters “visited” and “path” are initially not required to be passed as inputs but needs to be
            # updated recursively during the search implementation. If not required for your implementation purposes they can
            # be ignored and can be removed from the parameters.

    # Note2: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    # The function returns:
        # 1. If search_node is provided, the function returns 1 if the node is found and 0 if it is not found.
        # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.


    if start_node == search_node:
        return 1


    stack = []
    visited_nodes = []

    stack.append(start_node)

    while stack:
        curr_node = stack.pop()

        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)

            for connected_node in graph[curr_node]:
                if connected_node == search_node:
                    return 1

                stack.append(connected_node)

    
    if search_node == None:
        return visited_nodes

    return 0



    '''
    #Useful code snippets (not necessary but you can use if required)
    if start_node == search_node:
        return 1 # search node found

    if search_node is not None:
        return 0  # search node not found

    return path  # search node not provided, return entire path [list of nconst id's of nodes visited] 
    '''



def dijkstra(graph, start_node, end_node):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
        #1. If the end_node is not reachable from the start_node, the function returns 0.

        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
                #2.1 The first element is a list representing the shortest path from start_node to end_node.
                     #[list of nconst values in the visited order]
                #2.2 The second element is the total distance of the shortest path.
                     #(summation of the distances or edge weights between minimum visited nodes)
                #2.3 The third element is Hop Count between start_node and end_node.

    # Return the shortest path and distances
    dist = {}
    visitedSet = {}
    prevNode = {}

    #distance to each vertex is initially infinity
    for key in graph:
        dist[key] = 2147483647
        visitedSet[key] = False
        prevNode[key] = 0

    #distance to start node is 0
    dist[start_node] = 0

    #loop number of times equal to number of nodes
    for key1 in graph:



        #find the key with the min distance that has not been visited
        #min_node = end_node
        min = 2147483647
        for key in graph:
            if dist[key] < min and visitedSet[key] == False:
                min = dist[key]
                min_node = key
        #########################
        
        #set the status of this min node to visited
        visitedSet[min_node] = True

        #for every unvisited neighbor of the current node
        for key2 in graph[key1]:
            if visitedSet[key2] == False and dist[key2] > dist[key1] + graph[key1][key2]:
                
                #update the new shorst distance
                dist[key2] = dist[key1] + graph[key1][key2]

                #update the prev node list
                prevNode[key2] = key1
        
    #print(dist)

    #if dist to end node is still max then node is unreachable
    #print("end node is: " + str(end_node))
    #print("dist is: " + str(dist[end_node]))
    if dist[end_node] == 2147483647:
        print("Node Unreachable")
        return 0

    path = []

    #start with the ending node and add to the path
    curr_node = end_node
    path.append(curr_node)

    #go backward through the prev node dict and add to front of path list
    while(curr_node != start_node):
        curr_node = prevNode[curr_node]
        path.insert(0, curr_node)


    #print(path)

    #need to return shortest dist(path), total dist, hop count

    total_dist = dist[end_node]
    
    hop_count = len(path)-1
    
    return [path, total_dist, hop_count]







def DFSUtil(node,visitedSet, graph, tmpSet):
        # Mark the current node as visited and print it
        visitedSet.append(node)
        tmpSet.append(node)
        #Recur for all the vertices adjacent to this vertex
        for connected_node in graph[node]:
            if connected_node not in visitedSet:
                DFSUtil(connected_node,visitedSet, graph, tmpSet)


def fillOrder(node,visitedSet,stack,graph):

    #add node to visited set
    visitedSet.append(node)

    #for every connected node visit that by recursion
    for connected_node in graph[node]:
        if connected_node not in visitedSet:
            fillOrder(connected_node, visitedSet, stack, graph)

    #add vertex to the stack
    stack.append(node)





# (strongly connected components)
def kosaraju(graph, inverse_graph):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    #Note: Here you need to call dfs function multiple times so you can Implement seperate
         # kosaraju_dfs function if required.

    #The output:
        #list of strongly connected components in the graph,
          #where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    
    components = []


    stack = []
    visitedSet = []

    for node in graph:
        if node not in visitedSet:
            fillOrder(node, visitedSet, stack, graph)


    #reset the visited set
    visitedSet.clear()

    tmpSet = []

    while stack:
        top_of_stack = stack.pop()
        if top_of_stack not in visitedSet:
            DFSUtil(top_of_stack, visitedSet, inverse_graph, tmpSet)
            components.append(tmpSet)
            tmpSet.clear()


    return components
