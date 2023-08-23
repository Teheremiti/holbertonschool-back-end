#!/usr/bin/python3
"""Script to export data in the CSV format"""

import csv
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

    with open(f"{USER_ID}.csv", mode='w') as f:
        Emp_tasks = csv.writer(f, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_ALL)
        for task in fieldsTodo:
            if task.get('userId') == USER_ID:
                TASK_COMPLETED_STATUS = task['completed']
                TASK_TITLE = task['title']
                Emp_tasks.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                               TASK_TITLE])
