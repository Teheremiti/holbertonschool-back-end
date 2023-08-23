#!/usr/bin/python3
"""Script that exports all tasks from all employees in JSON format"""

import json
import requests


if __name__ == "__main__":

    response = requests.get("https://jsonplaceholder.typicode.com/users/")
    fieldsUser = response.json()

    USERS = []
    for user in fieldsUser:
        USERS.append((user.get('id'), user.get('username')))

    responseTodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    fieldsTodo = responseTodo.json()

    tasks = []
    for task in fieldsTodo:
        tasks.append((task.get('userId'), task.get('title'),
                      task.get('completed')))

    users_dict = dict()

    for user in USERS:
        user_tasks = []
        for task in values:
            if task[0] == user[0]:
                user_tasks.append({"username": user[1], "task": task[1],
                                   "completed": task[2]})
        users_dict[str(user[0])] = user_tasks

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(users_dict, f)
