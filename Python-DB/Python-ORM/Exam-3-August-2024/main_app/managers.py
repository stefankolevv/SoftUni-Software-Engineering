from django.db import models

class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return self.annotate(mission_count=models.Count('missions')).order_by('-mission_count', 'phone_number')
