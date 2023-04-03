import pandas as pd

class MovieNetwork:
    def __init__(self, name_movie_dict, nconst_ar_dr):
        self.graph = {} #graph dictionary initialization
        self.name_movie_dict = name_movie_dict #name_movie_dict is nothing but "title_dict" dictionary refer to above example in TitleDictionary.
        self.nconst_ar_dr = nconst_ar_dr #it is "profession_dict" dictionary refer to above example in TitleDictionary.


    def add_node(self, node):
        #write code to add node to the graph (dictionary data-structure)
        
        #if node is not already in the dictionary
        if self.graph.get(node) == None:
            self.graph[node] = {}
        else:
            print("Vertex already in dict")



    def add_edge(self, node1, node2, weight=1):
        #node 1, node 2: nconst id's
        #nconst_ar_dr is nothing but "profession_dict" dictionary refer to above example in TitleDictionary.
        #weight is number of common movie titles exists in node1 and node2
        #Before adding Edge weights you must follow the below Instructions:
            #1. consider only the node1->node2 connection or edge, only if node1 and node2 have more than 2 movies in common.
            #2. Let node1="actor" and node2="director" then node1->node2 edge should not be taken implies {actor:{director:6}} must not be taken.
                # But node2->node1 should be taken implies {director:{actor:6}} must be taken.
            #3. if node1 and node2 are assigned with both actors or directors then bi-directional edge must be added implies
                #{actor1:{actor2:4}} and {actor2:{actor1:4}} or {director1:{director2:7}} and {director2:{director1:7}} both ways are true
                #and must consider in dictionary.
        #write code to add edge to the graph implies add weight between node1 and node 2
        #Example weight assignment looks like:
        # {'nm1172995': {'nm0962553': 7}} here the weight 7 is nothing but the number of common
        #movies between two persons either actor/director (nm1172995 and nm0962553)

        #make sure both nodes are in the graph
        if self.graph.get(node1) == None or self.graph.get(node2) == None:
            print("Error one of the nodes are not in the graph")
            return

        if self.graph.get(node1).get(node2):
            print("Error edge already in graph")
            return

        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight
        


    def create_graph(self):
        #By following the above conditions create a graph (use only dictionary datastructure: self.graph)
        #example graph looks like:
          # {'nm0962553': {'nm8630849': 3,
          #     'nm1172995': 7,
          #     'nm8742830': 16,
          #     'nm6225202': 4,
          #     'nm4366294': 4},
          #    'nm8630849': {},
          #    'nm1172995': {'nm0962553': 7},
          #    'nm8742830': {'nm0962553': 16},
          #    'nm6225202': {}}
        graph = []

        return graph
    
    def printGraph(self):
        print(str(self.graph)) 


mn = MovieNetwork(1, 1)
mn.add_node("Brandon")
mn.add_node("Lauren")

mn.add_edge("Lauren", "Brandon", 10)
mn.add_edge("Brandon", "Lauren", 10)

mn.printGraph()