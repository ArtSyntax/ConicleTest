from django.db import models

class Todo(models.Model):
    STATUS = (
        ('P', 'Pending'),
        ('D', 'Done'),
    )

    subject = models.CharField(max_length=200)
    detail = models.CharField(max_length=500, blank=True, default='')
    status = models.CharField(max_length=1, choices=STATUS, default='P')

