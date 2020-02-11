#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: jobs.py

import sqlite3

from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


# Create the database
def create_a_database():
    # You can create a new database by changing the name within the quotes
    conn = sqlite3.connect('Github_Jobs_DB.db')
    # The database will be saved in the location where your 'py' file is saved
    c = conn.cursor()

    # Create the table - GitJobs
    c.execute('CREATE TABLE IF NOT EXISTS GitJobs\n'
              '        ([generated_id] INTEGER PRIMARY KEY,[Type] text, [URL] text, [Created_at] text,\n'
              '        [Company] text, [Company_URL], text, [Locations] text, [Title] text, [Description] text)')
    # Make sure you save the file
    conn.commit()
    # You have to close it when you are done as well
    conn.close()


# Put data into the table
def populate_table(cursor, data):
    for listing in data:
        # Insert a row of data
        cursor.execute('''INSERT INTO GitJobs (generated_id, Type, URL, Created_at, Company, Company_URL, Locations, 
        Title, Description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (listing['id'], listing['type'], listing['url'],
                                                                     listing['created_at'], listing['company'],
                                                                     listing['location'],
                                                                     listing['title'], listing['description']))


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    conn, cursor = open_db('Github_Jobs_DB.db')
    create_a_database()
    populate_table(cursor, data)
    close_db(sqlite3.Connection)

    if __name__ == '__main__':
        main()
