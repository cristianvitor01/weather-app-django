from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        """Show the actual city name on the dashboard"""
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
