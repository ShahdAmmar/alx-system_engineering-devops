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

    student_dicts = student_json[str(id)]
    if isinstance(student_dicts, list) and all(isinstance(item, dict) for item in student_dicts):
        print("USER_ID's value type is a list of dicts: OK")
    else:
        print("USER_ID's value type incorrect")


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
