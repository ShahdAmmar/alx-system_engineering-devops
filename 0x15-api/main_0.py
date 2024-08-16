#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check user information """

    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    num_lines = 0
    with open(str(id) + ".csv", 'r') as f:
        for line in f:
            if not line == '\n':
                num_lines += 1

    if total_tasks == num_lines:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
