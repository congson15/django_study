from django.db import models


# Create your models here.
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
