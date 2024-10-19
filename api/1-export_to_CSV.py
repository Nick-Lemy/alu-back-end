#!/usr/bin/python3
"""Module"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_id)

    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    employee_name = user_info["name"]
    employee_username = user_info["username"]
    task_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    with open(str(employee_id) + '.csv', "w") as file:
        [file.write('"' + str(employee_id) + '",' +
                    '"' + employee_username + '",' +
                    '"' + str(task["completed"]) + '",' +
                    '"' + task["title"] + '",' + "\n")
         for task in todos_info]
