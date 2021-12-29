from django.db import models


class City(models.Model):
    city = models.CharField(unique=True,max_length=20)
    approve = models.BooleanField(default=True)
    def __str__(self):
        return self.city


class Temperature(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField('date')
    temp = models.IntegerField()
    class Meta:
        unique_together = ["city", "date"]
    def __str__(self):
        return self.city.city








