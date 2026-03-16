from django.forms import ModelForm

from app.models import Task


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "status", "tags"]
