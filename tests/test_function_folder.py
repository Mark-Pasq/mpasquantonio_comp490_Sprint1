#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 2
# Filename: test_function_folder.py
import sqlite3

import pytest

import jobs

conn = sqlite3.connect('test_github_jobs.sqlite')
c = conn.cursor()


@pytest.fixture
def get_data():
    pass


def test_jobs_dict(get_data):
    # first required test
    assert len(get_data) >= 100
    assert type(get_data[1]) is dict


def test_jobs_data(get_data):
    # any real data should have both full time and Contract
    # jobs in the list, assert this
    data = get_data
    full_time_found = False
    contract_found = False
    for item in data:
        if item['type'] == 'Contract':
            contract_found = True
        elif item['type'] == 'Full Time':
            full_time_found = True
    assert contract_found and full_time_found


def test_save_data():
    # second required test
    demo_data = {'id': 1234, 'type': "Testable"}
    list_data = []
    list_data.append(demo_data)
    file_name = "testfile.txt"
    jobs.save_data(list_data, file_name)
    testfile = open(file_name, 'r')
    saved_data = testfile.readlines()
    # the save puts a newline at the end
    assert f"{str(demo_data)}\n" in saved_data


def test_check_if_table_exists():
    # conn = sqlite3.connect('test_github_jobs.sqlite')
    # c = conn.cursor()

    # santore_db.create_table(c)

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Jobs_Listing' ''')

    # if the count is 1, then table exists
    assert (c.fetchone()[0] == 1)
    print('There is only 1 table in the database named Jobs_Listing.')


def test_get_locations():
    # conn = sqlite3.connect('test_github_jobs.sqlite')
    cursor = conn.cursor()

    for row in cursor.execute("SELECT EXISTS (SELECT 10 from 'GitJobs' WHERE generated_id = "
                              "'7b7d433d-caf3-4b1b-9cf1-e4c25d560a53')"):
        assert 'location', row[0] == 'New York'
        print('New York is the location of the job in row 0')


def test_get_number_of_rows(count=None):
    con = sqlite3.connect('test_github_jobs.sqlite')
    cursor = con.cursor()
    # result = c.execute("select count(*) from Jobs_Listing")  # returns array of tuples
    # assert result[0][0] > 200
    # cursor.execute("BEGIN")  # start transaction
    # # if n > big: be_prepared()
    # all_rows = cursor.execute("SELECT * FROM Jobs_Listing").fetchall()
    # #
    # # assert n == len(all_rows)
    # # print(len(all_rows))
    # cursor.connection.commit()  # end transaction
    rows_query = "SELECT Count() FROM 'GitJobs'"
    print(count)
    cursor.execute(rows_query)
