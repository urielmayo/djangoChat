from django.urls import path

from users import views
urlpatterns = [
    path(
        route='users/login',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='users/logout',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='users/signup',
        view=views.SignUpView.as_view(),
        name='signup'
    ),
    path(
        route='update-profile/',
        view=views.ProfileUpdateView.as_view(),
        name='update-profile'
    )
]