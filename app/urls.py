from django.urls import path

from app.views import (
    index_view,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", index_view, name="index"),
    path("", index_view, name="index"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),

]

app_name = "app"
