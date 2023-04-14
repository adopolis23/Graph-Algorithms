import pandas as pd 
import json

from graph_creation import TitleDictionary
from graph_creation import MovieNetwork


td = TitleDictionary("imdb_network.csv")

mn = MovieNetwork(td.title_dict, td.profession_dict)
mn.create_graph()


from graph_algorithms import dijkstra


print(dijkstra(mn.graph, "nm0465106", "nm4337938"))

#print(str(mn.graph['nm0465106']))
#mn.printGraph()