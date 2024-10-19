#!/usr/bin/python3
"""export data in the CSV format"""
import sys
import requests
import csv

if __name__ == '__main__':
    """gather data from an api"""
    response_todos = requests.get(
        "https://jsonplaceholder.typicode.com/user/" + sys.argv[1] + "/todos"
    )
    data = response_todos.json()
    completed_tasks = []
    for i in data:
        if i['completed']:
            completed_tasks.append(i['title'])
    r = 'completed'

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    ).json()
    with open(f'USER_ID.csv', 'w', newline="") as file:
        csvwriter = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)  # create a csvwriter object
        for i in data:
            csvwriter.writerow([sys.argv[1], user["username"], i["completed"], i["title"]])
