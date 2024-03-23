# myapp/tasks.py
from celery import shared_task
from time import sleep

@shared_task
def my_task():
    for i in range(4):
        print("hello")
        sleep(i)
    return "Task Complete!"



