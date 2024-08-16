#!/usr/bin/python3
""" This python script exports data about all
    employees' tasks in a json format for a given ID"""
import json
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"

users = requests.get(url + 'users/')
users_json = users.json()

all_employees = dict()
for user in users_json:
    user_id = user.get('id')
    user_todos = requests.get(url + f'users/{user_id}/todos').json()

    user_tasks = []
    for task in user_todos:
        task_dict = {
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
                }
        user_tasks.append(task_dict)
    all_employees[str(user_id)] = user_tasks

with open('todo_all_employees.json', 'w') as fl:
    json.dump(all_employees, fl)
