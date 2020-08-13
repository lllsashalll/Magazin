from django.db import models


class Comment(models.Model):
    title = models.CharField(max_lenght=100)
    comment = models.TextField()
    name_user = models.DateTimeField()

    def __str__(self):
        return self.title
