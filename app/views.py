from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Index page")


class TaskListView:
    pass


class TaskCreateView:
    pass


class TaskUpdateView:
    pass


class TaskDeleteView:
    pass


class TagListView:
    pass


class TagCreateView:
    pass


class TagUpdateView:
    pass


class TagDeleteView:
    pass