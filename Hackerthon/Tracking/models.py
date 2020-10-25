from django.db import models
from django.contrib.auth.models import User
from Pickup.models import Ingredients
from django.utils import timezone

# Create your models here.

# 매장
class Store(models.Model):
    store_name = models.CharField(max_length=40)
    store_locate = models.CharField(max_length=250)

    def __str__(self):
        return self.store_name

# 지점 별 재고
class StoreStock(models.Model):
    store_name = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient_name = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    remain = models.IntegerField()

    def __str__(self):
        return self.store_name.store_name

# 배송 정보
class DeliverInfo(models.Model):
    deliver_address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deliverable = models.BooleanField(null=False)
    order_date = models.DateTimeField()

    def __str__(self):
        return self.user.username


# 주문한 재료 정보   
class DeliverIngList(models.Model):
    deliver_info = models.ManyToManyField(DeliverInfo)
    ingred_info = models.ManyToManyField(Ingredients)

