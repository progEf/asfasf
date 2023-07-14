from django.forms import ModelForm

from .models import photo_product, name_product, categoriy_product, description_product, price_product, \
    all_user_product, User
from django import forms


class UserName(ModelForm):
    def __init__(self ,*args, **kwargs):
        user = kwargs.pop('user')  # получаем текущего пользователя из параметров формы
        super().__init__(*args, **kwargs)

       # self.fields['id_user'].queryset = User.objects.filter(username= user)
        a = User.objects.filter(username=user).values_list('pk', flat=True).first()
        self.fields['id_user'].required = False





    class Meta:
        model = name_product
        fields = ['name', 'id_user']
        widgets = {
            'id_user': forms.HiddenInput(),
        }


class UserImage(ModelForm):
    def __init__(self ,*args, **kwargs):
        user = kwargs.pop('user')  # получаем текущего пользователя из параметров формы
        super().__init__(*args, **kwargs)

        self.fields['id_user'].required = False
        self.fields['id_name_product'].required = False



    class Meta:
        # To specify the model to be used to create form
        model = photo_product
        # It includes all the fields of model
        fields = '__all__'
        widgets = {
            'id_user': forms.HiddenInput(),
            'id_name_product': forms.HiddenInput()
        }
