#!/usr/bin/python3
"""Script to export data in JSON format"""

import json
import requests
import sys


if __name__ == "__main__":

    USER_ID = int(sys.argv[1])

    url_requestUser = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    responseUser = requests.get(url_requestUser)
    fieldsUser = json.loads(responseUser.content)

    USERNAME = fieldsUser.get('username')

    responseTodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    fieldsTodo = json.loads(responseTodo.content)

    Emp_tasks = {}
    tasks = []
    for task in fieldsTodo:
        if task.get('userId') == USER_ID:
            TASK_COMPLETED_STATUS = task['completed']
            TASK_TITLE = task['title']
            task_details = {"task": TASK_TITLE, "completed":
                            TASK_COMPLETED_STATUS, "username": USERNAME}
            tasks.append(task_details)
    Emp_tasks = {USER_ID: tasks}
    json_object = json.dumps(Emp_tasks)

    with open(f"{USER_ID}.json", mode='w') as f:
        f.write(json_object)
