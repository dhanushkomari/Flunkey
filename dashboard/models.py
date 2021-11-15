from django.db import models
from api.models import Bot

# Create your models here.

class Bot_location(models.Model):
    bot = models.OneToOneField(Bot, on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=500, decimal_places=4, blank = True, null = True)
    y = models.DecimalField(max_digits=50, decimal_places=4, blank = True, null=True)    
    angle = models.DecimalField(max_digits=50, decimal_places=4, blank = True, null = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Bot location'
        verbose_name = 'Bot locations'
    
    def __str__(self):
        return str(self.bot.name)
