from pipes import Template
#Import on the top:
#imports:
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView




# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class MenuPageView(TemplateView):
    template_name = 'menu.html'

#class LoginPageView(TemplateView):
 #   template_name = 'login.html'
 
class LoginPageView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        (self.request, user)
        return super().form_valid(form)

 
 

#class SignUpPageView(TemplateView):
#    template_name = 'signup.html'
    

class SignUpPageView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CartPageView(TemplateView):
    template_name = "cart.html"

class ProfileEditPageView(TemplateView):
    template_name = "ProfileEdit.html"