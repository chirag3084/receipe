from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = CloudinaryField("receipes")
    recipe_view_count = models.IntegerField(default=1)

    def __str__(self):
        return self.receipe_name
