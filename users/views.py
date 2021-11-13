from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy

from users.forms import SignUpForm
# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class LogoutView(auth_views.LogoutView):
    """LogoutView"""

class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)