from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render

from app.forms import TaskCreateForm, TagCreateForm
from app.models import Task, Tag


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
    model = Task
    success_url = reverse_lazy("app:task_list")


class TagListView(generic.ListView):
    pass


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("app:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("app:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag_list")