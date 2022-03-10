from django.db import models


class WaterModel(models.Model):
    """
    Water Model
    """
    name = models.CharField(max_length=100)
    rateOfFlow = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.name} @ {self.rateOfFlow}/sec"