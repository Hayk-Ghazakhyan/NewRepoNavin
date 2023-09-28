from django.db import models

# Create your models here.
class Destination:
    price: int
    name: str
    img: str
    desc: str
    offer: bool