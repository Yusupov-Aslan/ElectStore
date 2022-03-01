from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import RegisterView, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', logout_view, name="logout"),
    path('registration/', RegisterView.as_view(), name="registration"),
]
