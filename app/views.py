from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render

from app.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    pass


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