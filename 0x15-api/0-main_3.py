#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    task = None
    filename = 'student_output'
    count = 0
    with open(filename, 'r') as f:
        output = f.read()
        for i in resp:
            if (i['completed'] and i['userId'] == id):
                task = i['title']
                count += 1
                if output.find(task) is not -1:
                    print("Task {} in output: OK".format(count))
                else:
                    print("Task {} not in output".format(count))


if __name__ == "__main__":
    check_tasks(int(sys.argv[1]))
