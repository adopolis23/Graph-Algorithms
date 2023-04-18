import pandas as pd 
import json

from graph_creation import TitleDictionary
from graph_creation import MovieNetwork


td = TitleDictionary("imdb_network.csv")

mn = MovieNetwork(td.title_dict, td.profession_dict)
mn.create_graph()

with open("Graph_Output.json", "r",encoding="iso-8859-1") as file:
    data = json.load(file)


from graph_algorithms import dijkstra


print(dijkstra(mn.graph, "nm0465106", "nm1118718"))
print(data["testcase_3_2"])

#print(str(mn.graph['nm0465106']))
#mn.printGraph()