from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

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
    model = Tag


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


def task_toggle_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    task = Task.objects.get(pk=pk)
    task_status = not task.status
    task.save()
    return HttpResponseRedirect(reverse("app:task_list"))
