from django.db import models


class House(models.Model):
    name = models.CharField(max_length=20, default="Undefined")
    height = models.IntegerField(default=10)
    weight = models.IntegerField(default=10)
    location = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}, {self.location}"

    # def weight_in_grams(self):
    #     return int(self.weight) * 1000

    def height_weight(self):
        return f"Height: {self.height}, Weight: {self.weight}"
