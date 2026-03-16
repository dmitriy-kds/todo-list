from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Index page")


class TaskListView(generic.ListView):
    pass


class TaskCreateView(generic.CreateView):
    pass


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