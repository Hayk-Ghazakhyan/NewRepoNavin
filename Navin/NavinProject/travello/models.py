from django.db import models

# Create your models here.
class Destination(models.Model):
    

    price = models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    info_dest = models.TextField()

    def __str__(self) -> str:
        return self.name
    