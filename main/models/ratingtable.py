from django.db import models
from BladeIndex.settings import K


class RatingTable(models.Model):
    name = models.SlugField()

    def update_ratings(self, winner, looser, w_score, l_score):
        r_w = winner.rating(self)
        r_l = looser.rating(self)
        R_w = 10 ** (r_w/400)
        R_l = 10 ** (r_l/400)
        E_w = R_w/(R_w+R_l)
        E_l = R_l / (R_w + R_l)
        new_r_w = r_w + K*(1-E_w)
        new_r_l = r_l + K*((l_score/w_score) - E_l)
        winner.update_rating(self, new_r_w)
        looser.update_rating(self, new_r_l)
        return new_r_w, new_r_l
