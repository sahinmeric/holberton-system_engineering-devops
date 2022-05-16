#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    all_tasks = 0
    done_tasks = 0

    # Get the JSON dictionaries for requested user and all TODOs
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(uid)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    name = user.get("name")

    # Get all tasks and completed tasks numbers, and the user completed tasks
    completed_tasks = []
    for task in todos:
        if int(uid) == task.get('userId'):
            all_tasks += 1
            if task.get('completed') is True:
                done_tasks += 1
                completed_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'.format(name, done_tasks,
                                                          all_tasks))

    # Print all completed tasks' titles
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
