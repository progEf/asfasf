from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from register.forms import UserCreationForm_1


class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form':UserCreationForm_1()
            }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm_1(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)