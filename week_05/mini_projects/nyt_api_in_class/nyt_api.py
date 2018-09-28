import json
import sys
import requests
import os
from top_story import TopStory
import mysql.connector as mc


class MyApp:

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
        #We will load latest data into a "staging" table before putting into our archives. THerefore we want to Truncate first.
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
                #Below we insert each record into staging table
                self.data_insert(obj)
        except Exception as exc:
            print(exc)

        #Execute stored procedure to move data from staging into permanent table if there are any new records only to eliminate duplication.
        self.data_insert_perm()
        return data

    def db_connect(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=os.environ.get("MYSQL_PASSWORD"),
            database="api_in_class"
        )
        return mydb

    def data_insert_perm(self):
        mydb = self.db_connect()
        mycursor = mydb.cursor()

        try:
            mycursor.execute("CALL usp_nyt_top_stories()")

            mydb.commit()
        except Exception as exc:
            print(exc)
        finally:
            mycursor.close()
            mydb.close()

    def truncate_staging(self):
        mydb = self.db_connect()
        mycursor = mydb.cursor()

        try:
            mycursor.execute("TRUNCATE nyt_top_stories_staging")

            mydb.commit()
        except Exception as exc:
            print(exc)
        finally:
            mycursor.close()
            mydb.close()

    def data_insert(self, topstory):
        mydb = self.db_connect()
        mycursor = mydb.cursor()

        try:

            insert = "INSERT INTO nyt_top_stories_staging (title, abstract, published_date, short_url, image_url) VALUES (%s, %s, %s, %s, %s)"
            _tuple_of_values = (topstory.title, topstory.abstract, topstory.published_date, topstory.short_url, topstory.image_url)
            mycursor.execute(insert, _tuple_of_values)

            mydb.commit()
        except Exception as exc:
            print(exc)
        finally:
            mycursor.close()
            mydb.close()

    def get_results(self):

        mydb = self.db_connect()
        mycursor = mydb.cursor()

        try:
            mycursor.execute("SELECT * FROM nyt_top_stories")

            myresult = mycursor.fetchall()
            print(myresult)
            _list = []
            for x in myresult:
                _list_from_return = list(x)
                _list.append(_list_from_return)
                print(x)
            return _list

        except Exception as exc:
            print(exc)

        finally:
            mycursor.close()

            mydb.close()
        return myresult
