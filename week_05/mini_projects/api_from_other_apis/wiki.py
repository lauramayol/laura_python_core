# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON
import mysql.connector as mc
import sql_methods
from datetime import datetime


class WikiApp:

    mydb = sql_methods.SqlCommands('localhost', 'root', 'api_in_class')

    def load_movie_data(self):
        '''
            Truncates table according to table_name variable and re-populates from Wikidata source.
        '''
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

        table_name = "wikipedia_movies"

        self.mydb.exec_statement("TRUNCATE", table_name)

        header_list = results["head"]["vars"]
        data_list = []
        for result in results["results"]["bindings"]:
            inner_list = []
            for header in header_list:
                #data_list.append(result[header]["type"] )
                inner_list.append(result[header]["value"])
            data_list.append(tuple(inner_list))

        self.mydb.data_insert(table_name, tuple(header_list), data_list)

        return f"Inserted {len(data_list)} records on {datetime.now()}."

    def get_location(self, movie_name):
        '''
            Variables:
            movie_name (str) = name of movie to search in database. Search is case-sensitive but needs to match full string.

            Return value:
            Returns records from vw_wikipedia_movies in mydb that match movie_name variable.
        '''

        where_filter = f" WHERE movie_name='{movie_name}'"

        my_result = self.mydb.select_results("vw_wikipedia_movies", where_filter)

        return my_result
