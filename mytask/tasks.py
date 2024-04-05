# myapp/tasks.py
import requests
from celery import shared_task
from time import sleep

# @shared_task
# def my_task():
#     for i in range(4):
#         print("hello")
#         sleep(i)
#     return "Task Complete!"


@shared_task
def my_task():
    api_url = "https://jsonplaceholder.typicode.com/todos/"

    try:
        response = requests.get(api_url)
        status_code = response.status_code
        print(f"API Status Code: {status_code}")

        # Additional handling based on status code if needed
        if status_code == 200:
            print("API call successful!")
        else:
            print("API call failed!")

    except Exception as e:
        print(f"Error occurred: {e}")

    for i in range(4):
        print("hello")
        sleep(i)
    return "Task Complete!"

@shared_task
def my_task1():
    api_url = "https://jsonplaceholder.typicode.com/todos/"

    try:
        response = requests.get(api_url)
        status_code = response.status_code
        print(f"API Status Code: {status_code}")

        # Additional handling based on status code if needed
        if status_code == 200:
            print("API call successful!")
        else:
            print("API call failed!")

    except Exception as e:
        print(f"Error occurred: {e}")

    for i in range(4):
        print("hello")
        sleep(i)
    return "Task Complete!"
