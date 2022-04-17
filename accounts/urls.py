from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('customer_register', views.customer_register.as_view(), name= 'customer_register'),
    path('owner_register', views.PgOwner_register.as_view(), name= 'owner_register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_view, name='logout'),


]
