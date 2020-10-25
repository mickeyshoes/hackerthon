from django.db import models
from django.contrib.auth.models import User
from Main.models import Recipe

# Create your models here.

# 식자제 종류 분류
class ClassifyIngredient(models.Model):
    class_ingred = models.CharField(max_length=20)

    def __str__(self):
        return self.class_ingred

# 식자제
class Ingredients(models.Model):
    ingred_name = models.CharField(max_length=50) # 재료 이름
    ingred_images = models.ImageField(upload_to="images/ingredients", blank=True) # 재료 사진
    price = models.IntegerField() # 가격
    gross_weight = models.IntegerField() # 중량
    classify = models.ForeignKey(ClassifyIngredient, on_delete=models.CASCADE) # 재료 분류

    def __str__(self):
        return self.ingred_name

# 레시피에 속하는 재료들
class Cooking(models.Model):
    ingredients = models.ForeignKey(ClassifyIngredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

# 게시글
class Posting(models.Model):
    recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('pickup:post_detail', args=[self.id])

# 후기
class Review(models.Model):
    review_post_num = models.ForeignKey(Posting, on_delete=models.CASCADE)
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_image = models.ImageField(upload_to="images/review", blank=True)
    review_body = models.TextField()
    likes = models.ManyToManyField(
        User,
        through = 'ReviewLike',
        through_fields = ('review','user'),
        related_name = 'likes'
    )
# 후기 - 좋아요 기능
class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# 고객 QnA 댓글 형식으로 구현
class QAndA(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500)
