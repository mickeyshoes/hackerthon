from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Posting, QAndA, Review, ReviewLike, Cooking
from Main.models import Recipe
import json

# Create your views here.

def recipeDetail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    post = get_object_or_404(Posting, recipe_name=recipe)
    ingredients = Cooking.objects.filter(recipe=recipe)
    print(ingredients[0].ingredients)
    reviews = Review.objects.filter(review_post_num_id=id).order_by('-likes')
    Qnas = QAndA.objects.filter(posting_id=id)
    return render(request, "recipeDetail.html", {"post":post, "Qnas":Qnas, "reviews":reviews, "ingredients":ingredients })

def pickCreate(request):
    if request.method == 'POST':
        post = Posting()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    elif request.method == 'GET':
        return render(request, "pickNew.html")
    return redirect('pickup:pickHome')

def pickDelete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("pickup:pickHome")

def ingredientCreate(request):
    if request.method == 'POST':
        ingre = Ingredient()
        ingre.Ingredient_title = request.POST['title']
        ingre.Ingredient_body = request.POST['body']
        ingre.Ingredient_price = request.POST['price']
        ingre.Ingredient_stock = request.POST['stock']
        ingre.save()
    elif request.method == 'GET':
        return render(request, "ingredientNew.html")
    return redirect('pickup:pickHome')

def pickReviewCreate(request):
    if request.method == 'POST':
        return redirect('pickup:pickHome')
    elif request.method == 'GET':
        return render(request, "pickNewReview.html")
    return redirect('pickup:pickHome')

def pickQnaCreate(request, id):
    post = Posting.objects.get(pk=id)
    Qna = QAndA()
    comment = request.POST['Qna_comment']
    Qna.comment = comment
    Qna.posting = post
    Qna.user = request.user
    Qna.save()
    return redirect('pickup:recipeDetail', id=id)
    

def qnaDelete(request, id):
    qna = get_object_or_404(QAndA, pk=id)
    if permission_check(request.user.username, qna.user.username):
        qna.delete()
        
    return redirect('pickup:recipeDetail', id=qna.posting_id)


def reviewCreate(request, id):
    if request.method == "POST":
        posting = Posting.objects.get(pk=id)
        review = Review()
        review.review_post_num = posting
        review.review_body = request.POST["textfield"]
        review.review_user = request.user
        review.review_image = request.POST["review-img"]
        review.save()
        return redirect('pickup:recipeDetail', id=id)
    elif request.method == "GET":
        return render(request, "reviewCreate.html", {'id':id})

def reviewDetail(request, id):
    review = get_object_or_404(Review, pk=id)
    return render(request, "reviewDetail.html", {"review":review})

def review_update(request, id):
    review = get_object_or_404(Review, pk=id)
    if request.method == "POST":
        review.review_body = request.POST["textfield"]
        review.review_image = request.POST["review-img"]
        review.save()
        return redirect('pickup:recipeDetail', id=review.review_post_num_id)
    elif request.method == "GET":
        if permission_check(request.user.username, review.review_user.username):
            return render(request, "reviewUpdate.html", {"review":review})
        else:
            import json
            message = {
                'message':"본인만 수정 가능합니다."
            }
            return HttpResponse(json.dumps(message), content_type='application/json')

def reviewDelete(request, id):
    review = get_object_or_404(Review, pk=id)

    if permission_check(request.user.username, review.review_user.username):
        review.delete()
    return redirect('pickup:recipeDetail', id=review.review_post_num_id)


def reviewLike(request):
    id = request.POST.get('pk', None)
    review = get_object_or_404(Review, pk=id)
    review_like, review_like_created = review.reviewlike_set.get_or_create(user=request.user)

    if not review_like_created:
        review_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {
        'message': message,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")

def permission_check(login_id, user_id):
    if login_id != user_id:
        return False
    elif login_id is None:
        return False
    else:
        return True