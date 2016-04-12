from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length = 100)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated_at',)

