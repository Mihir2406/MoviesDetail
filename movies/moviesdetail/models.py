from platform import release
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from pandas import notnull

class Movi(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    release_date=models.IntegerField()
    imdb_rating=models.FloatField()
    duration=models.IntegerField()
    description=models.TextField()

    class Meta:
        db_table = "moviesdetailss"
