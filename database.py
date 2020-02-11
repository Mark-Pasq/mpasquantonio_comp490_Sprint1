import sqlite3
from typing import Tuple
import jobs


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def create_table(cursor):
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.Jobs_Listing (
           id INTEGER PRIMARY KEY,
           type TEXT,
           url TEXT,
           created_at TEXT,
           company TEXT,
           company_url TEXT,
           location TEXT,
           title TEXT,
           description TEXT
           );''')


def populate_table(cursor, data):
    for listing in data:
        # Insert a row of data
        cursor.execute('''INSERT INTO GitJobs (generated_id, Type, URL, Created_at, Company, Locations, Company_URL, 
        Title, Description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', (listing['generated_id'], listing['Type'],
                                                                     listing['URL'],
                                                                     listing['Created_at'], listing['Company'],
                                                                     listing['Company_URL'], listing['Locations'],
                                                                     listing['Title'], listing['Description']))


# def get_number_of_rows():
#     conn = sqlite3.connect('github_jobs.sqlite')
#     cursor = conn.cursor()
#     cursor.execute("BEGIN")  # start transaction
#     n = cursor.execute("SELECT COUNT() FROM GitJobs").fetchone()[0]
#     # if n > big: be_prepared()
#     cursor.execute("SELECT * FROM GitJobs").fetchall()
#     cursor.connection.commit()  # end transaction
#     # assert n == len(all_rows)
#     print(n)


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    data = jobs.get_github_jobs_data()
    conn, cursor = open_db("Github_Jobs_DB.db")
    create_table(cursor)
    populate_table(cursor, data)
    # get_number_of_rows()
    print(type(conn))
    close_db(conn)

    if __name__ == '__main__':
        main()
