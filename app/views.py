from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render

from app.forms import TaskCreateForm
from app.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("app:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("app:task_list")


class TaskDeleteView(generic.DeleteView):
    pass


class TagListView(generic.ListView):
    pass


class TagCreateView(generic.CreateView):
    pass


class TagUpdateView(generic.UpdateView):
    pass


class TagDeleteView(generic.DeleteView):
    pass