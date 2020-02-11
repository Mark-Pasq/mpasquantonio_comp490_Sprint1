#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev.
# Project1 Agile Sprint1
# Filename: test_jobs.py
import pathlib
import requests

url = 'https://jobs.github.com/positions.json'


def test_jobs():
    response = requests.get(url)
    assert response.status_code == 200
    print("The response is valid!")


def test_exist_file():
    file = pathlib.Path('jobs.txt')
    if file.exists():
        print("The file exists!")
    else:
        print("The file does not exist!")


def test_num_of_jobs():
    count = 0
    for i in range(1, 6):
        response = requests.get(url).json()
        count += len(response)
    assert count >= 100


def check_entry_in_dict(names=None):
    # response = requests.get(url).json()
    names.append({'company': 'DevsData', 'location': 'Oslo, Norway', 'type': 'Full Time'})
    names.append({'company': 'Analytics Fire', 'location': 'Remote', 'type': 'Full Time'})
    names.append({'company': 'Constructive', 'location': 'New York City', 'type': 'Full Time'})

    if not any(d['company'] == 'Constructive' and d['location'] == 'New York City' for d in names):
        print('Not exists!')
    else:
        print('Exists!')
