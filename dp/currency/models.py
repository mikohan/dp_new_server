from django.db import models

class UsdRate(models.Model):

    rate = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(auto_now_add=True, unique=True)

    class Meta:
        verbose_name = "Euro Rate"

    def __str__(self):
        return str(self.date)
