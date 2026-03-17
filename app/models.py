from django.db import models


class Task(models.Model):
    status_choices = {
        True: "Done",
        False: "Not done",
    }

    content = models.TextField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(choices=status_choices, default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        verbose_name_plural = "tasks"
        ordering = ["status", "-created_at"]

    def __str__(self):
        return (f"Task: {self.content}, "
                f"Status: {self.status}, "
                f"Created at: {self.created_at}")


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name
