#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev.
# Project1 Agile Sprint1 
# Filename: jobs.py

import json
from datetime import time
from typing import List, Dict
import requests


def get_github_jobs_data() -> List[Dict]:
    """retrieve github jobs data in form of a list of dictionaries after json processing"""
    all_data = []
    page = 1
    more_data = True
    while more_data:
        url = f'https://jobs.github.com/positions.json?page={page}'
        raw_data = requests.get(url)
        if "GitHubber!" in raw_data:  # sometimes if I ask for pages too quickly I get an error; only happens in testing
            continue  # trying continue, but might want break
        partial_jobs_list = raw_data.json()
        all_data.extend(partial_jobs_list)
        if len(partial_jobs_list) < 50:
            more_data = False
        time.sleep(.1)  # short sleep between requests so I dont wear out my welcome.
        page += 1
    return all_data

    save_my_data(python_obj)


def save_my_data(python_obj):
    # This function creates a text file, writes the json data to the file, and
    # saves the data back to the text file.
    with open('jobs.txt', 'w') as f:
        f.write(json.dumps(python_obj, sort_keys=False, indent=4))
    f.close()


# Main() includes a for loop that will iterate through the multiple pages of
# the json file.
def main():
    for i in range(1, 6):
        url = f'https://jobs.github.com/positions.json?page={i}'
        get_jobs(url)


if __name__ == '__main__':
    main()
