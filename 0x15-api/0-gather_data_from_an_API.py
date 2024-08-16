#!/usr/bin/python3
""" This python script returns information about
    employee's TODO list progress for a given ID"""
import requests
import sys


def get_employee_todo_list_progress(emp_id):
    """ This function gets information about the employee todo list progress
    and prints the completed tasks
    Args:
        emp_id: the employee ID
    """
    if __name__ == "__main__":
        url = "https://jsonplaceholder.typicode.com/"
        emp_id = sys.argv[1]

        user = requests.get(url + f'users/{emp_id}')
        user_json = user.json()
        emp_name = user_json.get('name')
        if emp_name is None:
            print('This employee doesn\'t exist. You entered invalid ID.')
            sys.exit()

        parameters = {'userId': emp_id}
        todos = requests.get(url + f'users/{emp_id}/todos')
        todos_json = todos.json()

        completed_tasks = [tsk for tsk in todos_json if tsk.get('completed')]
        comp_tasks = len(completed_tasks)
        totl_tasks = len(todos_json)
        print('Employee {} is done with tasks({}/{}):'.
              format(emp_name, comp_tasks, totl_tasks))
        for task in completed_tasks:
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: script_name <employee_id>')
    else:
        get_employee_todo_list_progress(sys.argv[1])
