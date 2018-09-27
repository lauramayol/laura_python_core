# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON


class Movies():

    def __init__(self, movie_name):
        self.movie_name = movie_name.lower()

    def get_location(self):

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

        sparql.setQuery("""#Movies and their narrative location on a map
        #defaultView:Map
        #removed: ?narrative_location
          #OPTIONAL { ?movie wdt:P577 ?publication_date. }
        SELECT ?movie ?movieLabel ?narrative_locationLabel ?coordinates WHERE {
           ?movie wdt:P840 ?narrative_location ;
                  wdt:P31 wd:Q11424 .
           ?narrative_location wdt:P625 ?coordinates .
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }""")
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            if result["movieLabel"]["value"].lower() == self.movie_name:
                movie_location_dict = result
                return movie_location_dict
