from django.db import models


class Markers(models.Model):
    address = models.CharField(max_length=200)
    desc = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
