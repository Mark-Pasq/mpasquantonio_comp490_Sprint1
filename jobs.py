#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev.
# Project1 Agile Sprint1 
# Filename: jobs.py

import json
import requests as req


def get_jobs(url=None):
    # The get() function requests the web to give some data that the user is 
    # looking for, ie an api.
    response = req.get(url)

    # Print statement that will send out a request of the response from 
    # a web server, and if good, will respond with 200.
    print(response.status_code)

    # The loads() function takes the json data and converts it to a string.
    python_obj = response.json()

    # This print line will will format the json data into dictionaries that 
    # are easily manageable.
    print(json.dumps(python_obj, sort_keys=False, indent=4))

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
