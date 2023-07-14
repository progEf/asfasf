from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_user = models.CharField(validators=[phoneNumberRegex], max_length=11, null=False)
    data_time = models.DateTimeField(auto_now_add=True, null=True)


class name_product(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    data_time = models.DateTimeField(auto_now_add=True, null=True)


class photo_product(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_name_product = models.ForeignKey(name_product, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    # upload_to='images'
class categoriy_product(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_name_product = models.ForeignKey(name_product, on_delete=models.CASCADE)
    id_photo_product = models.ForeignKey(photo_product, on_delete=models.CASCADE)
    Unit_dimensions = [
        ('bottle', 'bottle '),
        ('packaging', 'packaging')
    ]
    el = models.CharField(max_length=200, choices=Unit_dimensions, null=True)

class description_product(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_name_product = models.ForeignKey(name_product, on_delete=models.CASCADE)
    id_photo_product = models.ForeignKey(photo_product, on_delete=models.CASCADE)
    id_categoriy_product = models.ForeignKey(categoriy_product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)

class price_product(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_name_product = models.ForeignKey(name_product, on_delete=models.CASCADE)
    id_photo_product = models.ForeignKey(photo_product, on_delete=models.CASCADE)
    id_categoriy_product = models.ForeignKey(categoriy_product, on_delete=models.CASCADE)
    id_description_product = models.ForeignKey(description_product, on_delete=models.CASCADE)
    price = models.IntegerField()

class all_user_product(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_name_product = models.ForeignKey(name_product, on_delete=models.CASCADE)
    id_photo_product = models.ForeignKey(photo_product, on_delete=models.CASCADE)
    id_categoriy_product = models.ForeignKey(categoriy_product, on_delete=models.CASCADE)
    id_description_product = models.ForeignKey(description_product, on_delete=models.CASCADE)
    id_price_product = models.ForeignKey(price_product, on_delete=models.CASCADE)




