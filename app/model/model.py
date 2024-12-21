"""
docstring
"""

import sqlite3
import random

DEBUG_MODE = True

class DBModel:
    """
    docstring
    """
    def __init__(self, db=None):
        """
        Constructor
        """
        self.db = db

        if self.db is not None:
            self.connection = sqlite3.connect(self.db, check_same_thread=False)
            self.cursor = self.connection.cursor()

            query_existing_tables = 'SELECT name FROM sqlite_master WHERE type="table"'

            self.cursor.execute(query_existing_tables)
            self.table_name = str(self.cursor.fetchone()[0])

    # DEPRECATED
    # def setup_db(self, db):
    #     """
    #     set_db
    #     """
    #     self.db = db
    #     if self.db is not None:
    #         self.connection = sqlite3.connect('data.db')
    #         self.cursor = self.connection.cursor()

    #         query_existing_tables = 'SELECT name FROM sqlite_master WHERE type="table"'

    #         self.cursor.execute(query_existing_tables)
    #         self.table_name = str(self.cursor.fetchone()[0])

    def get_headers(self):
        """
        get headers alternative
        """
        query_headers = f'SELECT * FROM {self.table_name}'

        if DEBUG_MODE:
            print(f'[GUU8HC] Query: {query_headers}')

        self.cursor.execute(query_headers)
        headers = [description[0] for description in self.cursor.description]
        return headers

    # DEPRECATED
    # def get_headers(self):
    #     """
    #     (on-going) get headers
    #     """
    #     # query_headers = f'select group_concat(name, "|") from pragma_table_info("{self.table_name}")'
    #     query_headers = f'select name from pragma_table_info("{self.table_name}")'
    #     self.cursor.execute(query_headers)
    #     headers = self.cursor.fetchall()
    #     return headers

    def get_all_items(self):
        """
        get all data
        """
        query_select_all = f'SELECT * FROM {self.table_name}'

        if DEBUG_MODE:
            print(f'[GUU8HC] Query: {query_select_all}')

        self.cursor.execute(query_select_all)
        rows = self.cursor.fetchall()
        return rows

    # def get_item_by_team(self, team):
    #     """
    #     get data by name
    #     """
    #     query_select_by_product_team = f'SELECT * FROM {self.table_name} WHERE Team like "%{team}%"'

    #     self.cursor.execute(query_select_by_product_team)
    #     rows = self.cursor.fetchall()

    #     return random.choice(rows)

    # def get_item_by_name(self, name):
    #     """
    #     get data by name
    #     """
    #     query_select_by_product_name = f'SELECT * FROM {self.table_name} WHERE Name like "%{name}%"'

    #     self.cursor.execute(query_select_by_product_name)
    #     rows = self.cursor.fetchall()
    #     return random.choice(rows) if len(rows) > 0 else rows[0]
