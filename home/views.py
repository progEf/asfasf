import time

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import UserImage, UserName

from home.models import photo_product, name_product, categoriy_product, description_product, price_product, \
    all_user_product, User


def create_product_name(request):
    if request.method == 'POST':
        form = UserName(request.POST, user=request.user)
        if form.is_valid():
            data_1 = form.cleaned_data
            field_shop = data_1['name']
            print(field_shop)
            us = User.objects.get(username=request.user.username).id  # Узнаем usera сессии     ОСТАВИТЬ
            print(us)
            find_user = User.objects.filter(id=us).first()
            name_product.objects.create(name=field_shop, id_user=find_user)

            # form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/add_photo/')
    else:
        form = UserName(request.POST, user=request.user)
        return render(request, 'add_product/name_form.html', {'form': form})


def image_request(request):
    if request.method == 'POST':
        form = UserImage(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            data_1 = form.cleaned_data
            field_shop = data_1['image']
            us = User.objects.get(username=request.user.username).id  # Узнаем usera сессии     ОСТАВИТЬ
            find_user = User.objects.filter(id=us).first()

            us_prod_name = name_product.objects.filter(id_user=find_user).values_list('pk', flat=True)
            us_prod_name_1 = us_prod_name[::-1]
            us_prod_name_2 = us_prod_name_1[0]
            id_prod_name = name_product.objects.filter(pk=us_prod_name_2).first()

            photo_create = photo_product.objects.create(id_user=find_user, id_name_product=id_prod_name,
                                                        image=field_shop).id

            # Getting the current instance object to display in the template
            img_object = form.instance

            print(photo_create)
            sre = photo_product.objects.filter(id_user=find_user)
            # $ print(sre)
            print('-------------------------------')

            return render(request, 'add_product/image_form.html', {
                'form': form,
                'img_obj': img_object,
                'photo': sre
            })
    else:
        form = UserImage(request.POST, request.FILES, user=request.user)
        us = User.objects.get(username=request.user.username).id
        find_user = User.objects.filter(id=us).first()
        f = photo_product.objects.filter(id_user=find_user)

    return render(request, 'add_product/image_form.html', {'form': form,
                                                           'f': f})
