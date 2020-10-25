from django.contrib import admin
from Main.models import *
from Pickup.models import *
from Tracking.models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Recipe)
admin.site.register(ClassifyIngredient)
admin.site.register(Ingredients)
admin.site.register(Cooking)
admin.site.register(Posting)
admin.site.register(Review)
admin.site.register(QAndA)
admin.site.register(Store)
admin.site.register(StoreStock)
admin.site.register(DeliverInfo)
admin.site.register(DeliverIngList)
admin.site.register(ReviewLike)

