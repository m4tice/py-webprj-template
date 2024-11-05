"""
Data manager module
"""
import sqlite3

from app import app

class DataManager:
    """
    class DataManager:
    """
    def __init__(self, db=None):
        """
        Constructor
        """
        self.db = db

        if self.db is not None:
            self.connection = sqlite3.connect(self.db)
            self.cursor = self.connection.cursor()

            query_existing_tables = 'SELECT name FROM sqlite_master WHERE type="table"'

            self.cursor.execute(query_existing_tables)
            self.table_name = str(self.cursor.fetchone()[0])

    def setup_db(self, db):
        """
        set_db
        """
        self.db = db
        if self.db is not None:
            self.connection = sqlite3.connect('data.db')
            self.cursor = self.connection.cursor()

            query_existing_tables = 'SELECT name FROM sqlite_master WHERE type="table"'

            self.cursor.execute(query_existing_tables)
            self.table_name = str(self.cursor.fetchone()[0])

    def get_headers_alternative(self):
        """
        get headers alternative
        """
        query_headers = f'SELECT * FROM {self.table_name}'
        self.cursor.execute(query_headers)
        headers = [description[0] for description in self.cursor.description]
        return headers

    def get_headers(self):
        """
        (on-going) get headers
        """
        # query_headers = f'select group_concat(name, "|") from pragma_table_info("{self.table_name}")'
        query_headers = f'select name from pragma_table_info("{self.table_name}")'
        self.cursor.execute(query_headers)
        headers = self.cursor.fetchall()
        return headers

    def get_all_data(self):
        """
        get_all_data
        """
        query_select_all = f'SELECT * FROM {self.table_name}'
        self.cursor.execute(query_select_all)
        rows = self.cursor.fetchall()
        return rows
