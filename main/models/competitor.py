from django.db import models
from BladeIndex.settings import RATING_LOG_LENGTH


class Competitor(models.Model):
    name = models.CharField(max_length=50)

    def update_rating(self, table, value):
        self.rating_set.create(rating_table=table, value=value)
        ratings_to_keep = self.rating_set.filter(rating_table=table).order_by('-time')[:RATING_LOG_LENGTH]
        self.rating_set.filter(rating_table=table).exclude(pk__in=ratings_to_keep).delete()

    def rating(self, table):
        if self.rating_set.filter(rating_table=table).exists():
            return self.rating_set.filter(rating_table=table).order_by('-time').first().value
        else:
            return 1
