# two_factor/urls.py
from django.urls import path
from . import views  # adjust the import according to your views

app_name = 'two_factor'

urlpatterns = [
    # your url patterns here, for example:
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # add other url patterns as needed
]
