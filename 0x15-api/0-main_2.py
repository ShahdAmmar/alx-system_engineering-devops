#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line_formatting(id):
    """ Check student output formatting """

    todos_count = 0
    todos_done = 0

    resp = requests.get(todos_url).json()
    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']
    
    filename = 'student_output'
    with open(filename, 'r') as f:
        first = f.readline().strip()

    output = "Employee {} is done with tasks({}/{}):".format(name, todos_done, todos_count)

    if first == output:
        print("First line formatting: OK")
    else:
        print("First line formatting: Incorrect")


if __name__ == "__main__":
    first_line_formatting(int(sys.argv[1]))
