from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms



# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm#name of form
    success_url = reverse_lazy('login')#reverse lzzy because want to enter signup then change to login reverse will directly change to login
    template_name = 'accounts/signup.html'
