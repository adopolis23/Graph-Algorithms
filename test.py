import pandas as pd 
from graph_creation import TitleDictionary
from graph_creation import MovieNetwork

td = TitleDictionary("imdb_network.csv")

mn = MovieNetwork(td.title_dict, td.profession_dict)
mn.create_graph()

mn.printGraph()