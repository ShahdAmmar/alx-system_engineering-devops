#!/usr/bin/python3
"""
Check student JSON output
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check user info """
    
    with open(str(id) + '.json', 'r') as f:
        student_json = json.load(f)

    if student_json.get(str(id)) and len(student_json) == 1:
        print("Correct USER_ID: OK")
    else:
        print("Correct USER_ID: Incorrect")


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
