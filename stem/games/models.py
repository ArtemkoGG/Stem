from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='games_images/', null=True, blank=True)

    def __str__(self):
        return self.title
