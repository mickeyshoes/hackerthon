from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length = 100, unique=True)
    user_birth_year = models.IntegerField(default=0)
    user_birth_month = models.IntegerField(default=0)
    user_birth_day = models.IntegerField(default=0)
    userid = models.CharField(max_length=100)
    password = models.CharField(max_length =100)
    phonenumber = models.CharField(max_length =100)
    address = models.CharField(max_length=100)

# 레시피
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=40)
    recipe_image = models.ImageField(upload_to="images/Recipe", blank=True)

    def __str__(self):
        return self.recipe_name