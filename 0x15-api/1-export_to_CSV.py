#!/usr/bin/python3
""" This python script returns information about
    employee's TODO list to a csv file"""
import requests
import sys


def export_employee_todos_to_csv(emp_id):
    """ This function gets information about the employee todos
    and exports it to csv file
    Args:
        emp_id: the employee ID
    """
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + f'users/{emp_id}')
    user_json = user.json()
    if user_json == {}:
        print('This employee doesn\'t exist. You entered invalid ID.')
        sys.exit()
    username = user_json.get('username')

    todos = requests.get(url + f'users/{emp_id}/todos')
    todos_json = todos.json()

    fl_name = f'{emp_id}.csv'
    with open(fl_name, 'w') as fl:
        for task in todos_json:
            status = str(task.get('completed')).title()
            task_title = task.get('title')
            fl.write(f'"{emp_id}","{username}","{status}","{task_title}"\n')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: script_name <employee_id>')
    else:
        export_employee_todos_to_csv(sys.argv[1])
