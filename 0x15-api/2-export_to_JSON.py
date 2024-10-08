#!/usr/bin/python3
""" This python script exports data about
    employee's tasks in a json format for a given ID"""
import json
import requests
import sys


def export_employee_tasks_to_json(emp_id):
    """ This function exports data about
        employee's tasks in a json format
    Args:
        emp_id: the employee ID
    """
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + f'users/{emp_id}')
    user_json = user.json()
    if user_json == {}:
        print('This employee doesn\'t exist. You entered invalid ID.')
        sys.exit()

    todos = requests.get(url + f'users/{emp_id}/todos')
    todos_json = todos.json()

    total_tasks = []
    for task in todos_json:
        task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_json.get('username')
                }
        total_tasks.append(task_dict)

    total_tasks_json = {str(emp_id): total_tasks}

    fl_name = str(emp_id) + '.json'
    with open(fl_name, 'w') as fl:
        json.dump(total_tasks_json, fl)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: script_name <employee_id>')
    else:
        export_employee_tasks_to_json(sys.argv[1])
