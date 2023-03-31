import pandas as pd

class TitleDictionary:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.title_dict = self._create_title_dict()
        self.profession_dict = self._create_profession_dict()

    def _create_title_dict(self):
        # Dictionary structure:
            # key: nconst
            # value: list of movie_names(primaryTitle's) actors/directors involved in
        #Create a dictionary in the format:
        #{nconst:[movie_names actors/directors involved in], here the actor/director is determined by id: nconst}
        #example dictionary looks like:
        # {'nm6551690': ['The Dreaded Hong Kong SneezeThe Great Bank Robbery',
        #   'The Reluctant RobotThe Royal Foil',
        #   'Theres No Business Like Snow Business'],
        #
        #   'nm8002705': ['The Awful Awakening of Claudius Brodequin',
        #   'The Dreaded Arrival of Captain Tardivaux',
        #   'The Glorious Triumph of Barthelemey Piechut',
        #   'The Magnificent Idea of Barthelemey Piechut the Mayor',
        #   'The Painful Infliction of Nicholas the Beadle',
        #   'The Scandalous Outcome of a Night of Destruction',
        #   'The Spirited Protest of Justine Pulet',
        #   'The Triumphant Inauguration of a Municipal Amenity']}
        title_dict = {}

        #for each row in the dataframe
        for index, row in self.df.iterrows():

            #if that person does not already have a list in the dictionary
            if title_dict.get(row['nconst']) == None:
                title_dict[row['nconst']] = [row['primaryTitle']]
            
            #if this person does already have a list in the dict
            else:
                title_dict[row['nconst']].append(row['primaryTitle'])


        #return the Created {nconst:[movie_titles]} dictionary
        return title_dict 




    def _create_profession_dict(self):

        # Dictionary structure:
            # key: nconst
            # value: actors/directors names with tail as '_a' or '_d'
        #Create a dictionary in the format:
        #{nconst:[actors/directors names], here the actor/director is determined by id: nconst}
        #while creating this dictionary values put _d at end of the name to indicate the person name as director and _a to represent the actor.
        #See the below example to understand more clearly.
        #example dictionary looks like:
        # {'nm0465106': 'Hal Roach Jr._d',
        #  'nm6081065': 'Benjamin H. Kline_d',
        #  'nm0962553': 'William Asher_d',
        #  'nm4337938': 'Rod Serling_a',
        #  'nm5829291': 'Sydney Newman_d',
        #  'nm7171552': 'Wolfgang Menge_a',
        #  'nm0231693': 'Blake Edwards_d',
        #  'nm6446679': 'Bob Wehling_a'}

        profession_dict = {}


        #for each row in the dataframe
        for index, row in self.df.iterrows():

            suffix = ""
            if row['primaryProfession'] == "director":
                suffix = "_d"
            else:
                suffix = "_a"

            #if this person is not in the dict already
            if profession_dict.get(row['nconst']) == None:

                #add their name to the dict plus the suffix
                profession_dict[row['nconst']] = row['primaryName'] + suffix
            
            #if this person is in the dict already -Dont think this path is taken
            else:
                continue

        
        print(profession_dict['nm0465106'])

        #return the Created {nconst:person_name_a/d} dictionary
        return profession_dict




td = TitleDictionary('imdb_network.csv')








'''
dict = {}


nconst = ['1', '2', '3', '4', '1', '2']

for x in nconst:

    if dict.get(x) == None:
        print("Not in dict")
        dict[x] = [0]
    else:
        print("In dict")
        dict[x].append(0)


print(dict.get('1'))
'''

