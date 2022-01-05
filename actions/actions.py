from typing import Any, Text, Dict, List
import urllib.request, json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, Ques, ans):
    conn.execute("INSERT INTO Qdata (Ques, Ans) VALUES ({}, {})".format(Ques, ans))
    conn.commit()
    print("----------------------------------------------------------------")
    cursor = conn.execute("SELECT Ques, Ans from Qdata")
    for row in cursor:
        print ("Ques = ", row[0])
        print ("Ans = ", row[1])
        print()
    print("----------------------------------------------------------------")
    conn.close()
    print ("Data added successfully")

class FaqEdu(Action):
    def name(self) -> Text:
        return "faq_edu_custom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # to get intent of user message
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message predicted by Rasa ",_intent)

        print(tracker.latest_message['text']) # to get user typed message 

        Ques = json.dumps(tracker.latest_message['text'])
        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        # print('tracker latest message', tracker.latest_message['response_selector'])
        # print(' ')
        # print('---', tracker.latest_message['response_selector'].keys())
        # print('   ')
        print("retrieval we found (i.e intent response key ) ",intent_found)

        # confidence of retrieval intent we found
        retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['response']['confidence']*100
        print(f"retrieval_intent_confidence we found was {retrieval_intent_confidence}")

        intent_found = f'utter_{eval(intent_found)}'
        print('after adding utter we found -- ', intent_found)

        print(domain['responses'][intent_found][0]['text'])
        ans = json.dumps(domain['responses'][intent_found][0]['text'])

# -------------------------------------------------------------------------------
        # conn = sqlite3.connect('test.db')
        # print ("Opened database successfully")
        # conn.execute('''CREATE TABLE Qdata
        #         (Ques           TEXT    NOT NULL,
        #         Ans            TEXT     NOT NULL);''')
        # print ("Table created successfully")
        # conn.close()
        database = "./actions/database/pythonsqlite.db"
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Qdata (Ques   TEXT    NOT NULL,
                                                                         Ans    TEXT    NOT NULL); 
                                    """
        # create a database connection
        conn = create_connection(database)
        # create tables
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)
            insert_data(conn, Ques, ans)
        else:
            print("Error!")

        # try:
            # conn.execute("INSERT INTO Qdata (Ques, Ans) VALUES ({}, {})".format(Ques, ans))
            # conn.commit()
            # print ("Records created successfully")
            # conn.close()
            # conn = sqlite3.connect('test.db')
            # print ("Opened database successfully")

            # cursor = conn.execute("SELECT Ques, Ans from Qdata")
            # for row in cursor:
            #     print ("Ques = ", row[0])
            #     print ("Ans = ", row[1])

            # print ("Operation done successfully")
            # conn.close()
        # except Exception as e:
        #     print(e)
        dispatcher.utter_message(response = intent_found) # use response for defining intent name
        return []