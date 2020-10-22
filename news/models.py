import datetime
import random

from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    url = models.CharField(max_length=30, default='test', editable=False)
    date = models.DateField(default= datetime.date.today(), editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:  # TODO
            suffix = random.randint(0, 100000)
            prefix = self.date.strftime('%Y%m%d')
            self.url = prefix + '-' + str(suffix)
        super(News, self).save(*args, **kwargs)
