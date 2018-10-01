import json
import sys
import requests
import os
from top_story import TopStory
import mysql.connector as mc
import sql_methods


class MyApp:

    mydb = sql_methods.SqlCommands('localhost', 'root', 'api_in_class')

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        if method == 'GET' and path == "/stories":
            return json.dumps(self.get_results())
            # do something
            # remember to close mydb connection
        elif method == 'GET' and path == "/load":
            return json.dumps(self.retrieve_top_stories())

        return "Your request is invalid, please try new URL"

    def retrieve_top_stories(self):
        r = requests.get("http://api.nytimes.com/svc/topstories/v2/home.json?api-key=117db68468bc43c69858e6880a2eb947", json=True)
        data = r.json()
        list_of_results = data['results']
        list_of_custom_top_stories = []
        # We will load latest data into a "staging" table before putting into our archives. THerefore we want to Truncate first.
        self.truncate_staging()
        try:
            for article in list_of_results:
                title = article['title']
                abstract = article['abstract']
                published_date = article['published_date']
                short_url = article['short_url']
                width = 0
                image_url = ""
                for image in article['multimedia']:
                    if image['width'] > width:
                        image_url = image['url']
                        width = image['width']

                obj = TopStory(title, abstract, published_date, short_url, image_url)
                list_of_custom_top_stories.append(obj)
                # Below we insert each record into staging table
                self.data_insert(obj)
        except Exception as exc:
            print(exc)

        # Execute stored procedure to move data from staging into permanent table if there are any new records only to eliminate duplication.
        self.data_insert_perm()
        return data

    def data_insert_perm(self):
        self.mydb.exec_statement("CALL", "usp_nyt_top_stories")

    def truncate_staging(self):
        self.mydb.exec_statement("TRUNCATE", "nyt_top_stories_staging")

    def data_insert(self, topstory):
        _tuple_of_headers = ("title", "abstract", "published_date", "short_url", "image_url")

        _tuple_of_values = [(topstory.title, topstory.abstract, topstory.published_date, topstory.short_url, topstory.image_url)]

        self.mydb.data_insert("nyt_top_stories_staging", _tuple_of_headers, _tuple_of_values)

    def get_results(self):
        my_result = self.mydb.select_results("vw_nyt_top_stories")

        return my_result
