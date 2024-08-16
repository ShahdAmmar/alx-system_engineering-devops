#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line(id):
    """ Fetch number of tasks """

    todos_count = 0
    todos_done = 0

    resp = requests.get(todos_url).json()
    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1

    filename = 'student_output'
    with open(filename, 'r') as f:
        first = f.readline().strip()
        
    if "{}/{}".format(todos_done, todos_count) in first:
        print("To Do Count: OK")
    else:
        print("To Do Count: Incorrect")


if __name__ == "__main__":
    first_line(int(sys.argv[1]))
