from django.contrib import admin
from .models import Competitor, Rating, RatingTable

admin.site.register(Competitor)
admin.site.register(Rating)
admin.site.register(RatingTable)
