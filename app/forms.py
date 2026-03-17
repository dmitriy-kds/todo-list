from django.forms import ModelForm

from app.models import Task, Tag


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "status", "tags"]


class TagCreateForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
