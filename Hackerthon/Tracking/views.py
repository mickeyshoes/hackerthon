from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from Main.models import *
from Pickup.models import *

# Create your views here.

def main(request):
    user_id = request.user


    return render(request, "deliverCheck.html")

def getUserAllDeliverInfo(request):
    datalist = DeliverInfo.objects.filter(user=request.user)
    print(datalist)
    deliver_list = DeliverIngList.objects.filter(deliver_info=datalist)
    print(request.user)
    print(deliver_list)
    return render(request, "deliverCheck.html", {'datalist':deliver_list})

def getUserTrueDeliverInfo(request):
    user_id = request.user
    datalist = DeliverInfo.objects.filter(user=user_id, deliverable=True)

    return render(request, "deliverCheck.html", {"datalist":datalist})

def getUserFalseDeliverInfo(request):
    user_id = request.user
    datalist = DeliverInfo.objects.filter(user=user_id, deliverable=False)

    return render(request, 'deliverCheck.html', {"datalist":datalist})

def getUserOrder(request, id):

    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=id)
        ingredients = Cooking.objects.filter(recipe=recipe)
        recipe_ingred = {}
        ingred_name = []
        ingred_index = []
        for i in ingredients:
            ingred_name.append(i.ingredients.class_ingred)
            ingred_index.append(i.ingredients.id)

        for j in range(len(ingred_name)):
            recipe_ingred[ingred_name[j]] = Ingredients.objects.filter(classify=ingred_index[j])
        print(recipe_ingred)

        for k in range(len(recipe_ingred)):
            temp = recipe_ingred[ingred_name[k]]
            temp_list = []
            for l in range(len(temp)):
                temp_list.append(temp[l].ingred_name)
            recipe_ingred[ingred_name[k]] = temp_list

        print(recipe_ingred)

        return render(request, 'order.html', {"recipe_ingred":recipe_ingred.items() ,'recipe':recipe})


def check_order_list(request):

    order_list = []

    if request.method == 'POST':
        classify_ingredients = ClassifyIngredient.objects.all()
        print(classify_ingredients)
        for i in classify_ingredients:
            if request.POST[i.class_ingred]:
                order_list.append(request.POST[i.class_ingred])
        #제품 리스트
        print(order_list)
        order_price = []
        #제품 가격을 알아보자
        for i in range(len(order_list)):
            Ingredients.objects.filter(ingred_name=order_list[i])
    
        return render(request, 'complete.html')

def addOrderPrice(request):

    order_list = []

    if request.method == 'POST':
        classify_ingredients = ClassifyIngredient.objects.all()
        print(classify_ingredients)
        for i in classify_ingredients:
            if request.POST[i.class_ingred]:
                order_list.append(request.POST[i.class_ingred])
        #제품 리스트
        print(order_list)
        order_price = []
        #제품 가격을 알아보자
        for i in range(len(order_list)):
            Ingredients.objects.filter(ingred_name=order_list[i])

        return HttpResponse(order_price)


        # 배송 정보
# class DeliverInfo(models.Model):
#     deliver_address = models.CharField(max_length=300)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     deliverable = models.BooleanField(null=False)
#     order_date = models.DateTimeField()

#     def __str__(self):
#         return self.user.username


# 주문한 재료 정보   
# class DeliverIngList(models.Model):
#     deliver_info = models.ManyToManyField(DeliverInfo)
#     ingred_info = models.ManyToManyField(Ingredients)
        
        # print(request.POST['key'])

    # if request.method == 'GET':
    #     print(request.POST['key'])
    #     print(request.POST['key'])

    # info = DeliverInfo()
        
    # info.user = request.user
    # info.deliver_address = form.cleaned_data['deliver_address']
    # info.order_date = timezone.now()
    # info.save()

    # order_list = DeliverIngList()
    # order_list.deliver_info = info
    # ingred_list = Cooking.objects.get(recipe_name='라면')
    # order_list.ingred_info = ingred_list.ingredients.all()
    # order_list.save()



def getClientIp(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
        print('get real IP')
    else:
        ip =request.META.get("REMOTE_ADDR")
        print('get inner network IP')

    from ipware import get_client_ip
    client_ip , is_routable = get_client_ip(request)
    if client_ip is None:
        print("can't get ip addr")
    else:
        if is_routable:
            print(is_routable)
        else:
            print(client_ip)


    return HttpResponse(ip)
