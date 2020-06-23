from django.db import models

# Create your models here.
class Food(models.Model):
    fdc_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=200, default='N/A')
    kcal = models.FloatField()

    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()

#    fiber = models.FloatField()
    water = models.FloatField()

    calcium = models.FloatField()
    magnesium = models.FloatField()
    potassium = models.FloatField()
    #sodium = models.FloatField()

    #vitamin_c = models.FloatField()
    #riboflavin = models.FloatField()

    def __str__(self):
        return self.name
    