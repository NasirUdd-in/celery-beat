# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .tasks import my_task



# def index(request):
#     my_task.delay()
#     return HttpResponse("Task Started!")


# def schedule_task(request):
#     interval, _ = IntervalSchedule.objects.get_or_create(
#         every=30,
#         period=IntervalSchedule.SECONDS,

#     )

#     PeriodicTask.objects.create(
#         interval=interval,
#         name="my-schedule",
#         task="mytask.tasks.my_task"
#     )
#     return HttpResponse("Task scheduled!")

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
def schedule_task(request):
    if request.method == 'POST':
        interval_value = request.POST.get('interval')

        interval, _ = IntervalSchedule.objects.get_or_create(
            every=int(interval_value),
            period=IntervalSchedule.SECONDS,
        )

        task_name = "my-schedule"

        # Check if a task with the same name already exists
        existing_task = PeriodicTask.objects.filter(name=task_name).first()

        if existing_task:
            # If a task with the same name exists, update its interval
            existing_task.interval = interval
            existing_task.save()
            return render(request, 'test.html')
        else:
            # If no task with the same name exists, create a new task
            PeriodicTask.objects.create(
                interval=interval,
                name=task_name,
                task="mytask.tasks.my_task"
            )
            return render(request, 'test.html')
    else:
        return render(request, 'test.html')

# from .forms import AdditionForm
# from .tasks import add_numbers





# def add_numbers_view(request):
#     if request.method == 'POST':
#         form = AdditionForm(request.POST)
#         if form.is_valid():
#             number1 = form.cleaned_data['number1']
#             number2 = form.cleaned_data['number2']
#             delay_minutes = form.cleaned_data['delay_minutes']
#             # Convert minutes to seconds
#             delay_seconds = delay_minutes * 60
#             # Invoke Celery task with input values and delay
#             add_numbers.apply_async(args=[number1, number2], countdown=delay_seconds)
#             return render(request, 'success.html')
#     else:
#         form = AdditionForm()
#     return render(request, 'addition_form.html', {'form': form})

# views.py

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.conf import settings
# from .forms import ScheduleUpdateForm
# from datetime import timedelta
# import subprocess

# def update_schedule(request):
#     if request.method == 'POST':
#         form = ScheduleUpdateForm(request.POST)
#         if form.is_valid():
#             schedule_interval = form.cleaned_data['schedule_interval']
#             if schedule_interval <= 0:
#                 return JsonResponse({'error': 'Invalid schedule interval'})

#             # Update CELERY_BEAT_SCHEDULE
#             settings.CELERY_BEAT_SCHEDULE['task-name']['schedule'] = timedelta(seconds=schedule_interval)

#             # Signal Celery Beat to reload the schedule
#             subprocess.run(['celery', '-A', 'autotask', 'beat', '-l', 'info', '--detach'])

#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'error': 'Form validation failed'})
#     else:
#         form = ScheduleUpdateForm()
#         return render(request, 'update_schedule.html', {'form': form})


# myapp/views.py
# from django.shortcuts import render
# from .models import TaskResult

# def task_results_view(request):
#     results = TaskResult.objects.all()
#     return render(request, 'task_results.html', {'results': results})


# from celery import shared_task


# @shared_task
# def add(x, y):
# 	return x + y
