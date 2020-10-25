from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pickup'

urlpatterns = [
    path('reviewLike/', views.reviewLike, name="reviewLike"),
    path('recipeDetail/<int:id>', views.recipeDetail, name="recipeDetail"),
    path('pickCreate/', views.pickCreate, name="pickCreate"),
    path('ingreCreate/', views.ingredientCreate, name="ingredientCreate"),
    path('pickDelete/<int:id>', views.pickDelete, name="pickDelete"),
    path('pickReviewCreate/', views.pickReviewCreate, name="pickReviewCreate"),
    path('pickQnaCreate/<int:id>', views.pickQnaCreate, name="pickQnaCreate"),
    path('qnaDelete/<int:id>', views.qnaDelete, name="qnaDelete"),
    path('reviewCreate/<int:id>', views.reviewCreate, name="reviewCreate"),
    path('reviewDetail/<int:id>', views.reviewDetail, name="reviewDetail"),
    path('review_update/<int:id>', views.review_update, name="review_update"),
    path('reviewDelete/<int:id>', views.reviewDelete, name="reviewDelete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
