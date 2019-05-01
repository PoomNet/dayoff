from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_login,name='login'),
    path('formoff/', views.formoff,name='formoff'),
    path('status/', views.status,name='status'),
path('logout/', views.my_logout,name='logout'),
]