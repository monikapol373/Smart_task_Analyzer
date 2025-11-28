# from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

def home(request):
    return render(request, "tasks/smart_task_analyzer.html")

def calculate_priority(task, strategy):
    due_date = datetime.strptime(task["due_date"], "%Y-%m-%d")
    days_left = (due_date - datetime.now()).days
    importance = task["importance"]
    hours = task["estimated_hours"]

    if strategy == "fastest":
        score = 100 / (hours + 1)
    elif strategy == "impact":
        score = importance * 10
    elif strategy == "deadline":
        score = max(1, 50 - days_left)
    else:  # smart balance
        score = (importance * 2) + (max(1, 30 - days_left)) + (10 / (hours + 1))

    return score

@api_view(["POST"])
def analyze_tasks(request):
    tasks = request.data.get("tasks", [])
    strategy = request.data.get("strategy", "smart")

    for task in tasks:
        task["priority_score"] = calculate_priority(task, strategy)

    sorted_tasks = sorted(tasks, key=lambda x: x["priority_score"], reverse=True)
    return Response(sorted_tasks)

