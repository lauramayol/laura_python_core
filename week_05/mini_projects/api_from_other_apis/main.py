import tweet
import wiki
import json


class MyApp:

    my_movie = wiki.WikiApp()

    def dispatch(self, environ):
        '''
            This app only supports GET requests.

            Path '/movie' will call movie_locations method and return results according to query given in API call.

            Path '/load' will refresh movie data using my_movie.load_movie_data method.
        '''
        #Initialize variables from API call.
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']

        #Format query to replace '%20' with spaces
        query_formatted = query.replace('%20', ' ')

        # Get movie_location details based on query
        if method == 'GET' and path == "/movie":
            return json.dumps(self.movie_locations(query_formatted))
        # Refresh movie data in MySQL database.
        elif method == 'GET' and path == "/load":
            return json.dumps(self.my_movie.load_movie_data())

        #Any other calls will be invalid.
        return "Your request is invalid, please try new URL."

    def movie_locations(self, user_input):
        '''
            Variables:
            user_input (str) = movie name

            Return value:
            Return narrative location of the user_input and current Twitter trends for its nearest location.
        '''
        try:
            # Get narrative location from mySQL database. This data is sourced from Wiki https://query.wikidata.org/sparql
            movie_location = self.my_movie.get_location(user_input)
            return_value = {"MovieDetails": movie_location[0][:4]}
            movie_coord_full = movie_location[0][4]
        except:
            return "Not found. Please enter another movie name in your query."
        else:
            # The coordinates come in this format: (long lat)
            movie_format = movie_coord_full.replace(')', '').replace('(', '')
            movie_coord = movie_format.split()

            # Get trends for nearest location in Twitter.
            my_trend = tweet.Trends()
            my_api = my_trend.set_tweep_connection()

            return_value["TwitterTrends"] = my_trend.get_location_trends(my_api, movie_coord[1], movie_coord[0])
            return return_value
