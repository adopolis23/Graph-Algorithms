import pandas as pd 
import json

from graph_creation import TitleDictionary
from graph_creation import MovieNetwork


td = TitleDictionary("imdb_network.csv")

mn = MovieNetwork(td.title_dict, td.profession_dict)
mn.create_graph()


with open("Graph_Output.json", "r") as file:
    data = json.load(file)


print(mn.graph["nm0465106"])
print(data["movie_network_test"]["nm0465106"])


#print(str(mn.graph['nm0465106']))
#mn.printGraph()