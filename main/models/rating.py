from django.db import models
from main.models import RatingTable, Competitor


class Rating(models.Model):
    value = models.IntegerField()
    rating_table = models.ForeignKey(to=RatingTable, on_delete=models.CASCADE)
    competitor = models.ForeignKey(to=Competitor, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

