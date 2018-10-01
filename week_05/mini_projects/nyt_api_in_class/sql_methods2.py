
import mysql.connector as mc
import os


class SqlCommands():

    def __init__(self, host, user, db):
        self.host = host
        self.user = user
        self.db = db

    def db_connect(self):
        mydb = mc.connect(
            host=self.host,
            user=self.user,
            password=os.environ.get("MYSQL_PASSWORD"),
            database=self.db
        )
        return mydb

    def exec_statement(self, action, db_object):
        '''
            action: can be TRUNCATE, CALL, DROP...
            object: specify the table name or stored procedure
        '''
        mydb = self.db_connect()
        mycursor = mydb.cursor()

        if action == "call":
            suffix = "()"
        else:
            suffix = ""

        statement = f"{action.upper()} {db_object} {suffix}"

        try:
            mycursor.execute(statement)

            mydb.commit()
        except Exception as exc:
            print(exc)
        else:
            print(f"'{statement}' has been executed.")
        finally:
            mycursor.close()
            mydb.close()

    def data_insert(self, db_object, db_object_tuple, data_tuple):
        '''
            Recieves a db_object that must be a table and inserts records based on data tuple.
        '''
        mydb = self.db_connect()
        mycursor = mydb.cursor()

        header_tuple = self.create_insert_tuple(db_object_tuple, "%s")

        insert_statement = f"INSERT INTO {db_object} {header_tuple[0]} VALUES {header_tuple[1]}"

        try:

            mycursor.execute(insert_statement, data_tuple)

            mydb.commit()
        except Exception as exc:
            print(exc)
        finally:
            mycursor.close()
            mydb.close()

    def create_insert_tuple(self, header_tuple, delimeter):
        '''
            Iterates through the header tuple to create text that will be used to insert data into table.
        '''
        header_str = self.pre_create_tuple(header_tuple, True)
        value_str = self.pre_create_tuple(header_tuple, False, delimeter)

        return (header_str, value_str)

    def pre_create_tuple(self, t, is_header, delim=""):
        '''
            Iterates through the header tuple to create text that will be used to insert data into table.
        '''
        formatted_str = "("
        for i in t:
            if is_header:
                pre = i
            else:
                pre = delim
            formatted_str += pre + ", "

        formatted_str += ")"
        # remove final commas
        return_value = formatted_str.replace(", )", ")")

        return return_value

    def select_results(self, db_object):
        '''
            Returns a list for all items found in db_object
        '''
        mydb = self.db_connect()
        mycursor = mydb.cursor()

        statement = f"SELECT * FROM {db_object}"

        try:
            mycursor.execute(statement)

            myresult = mycursor.fetchall()
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
