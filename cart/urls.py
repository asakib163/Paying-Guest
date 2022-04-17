from django.urls.conf import path
from . import views
urlpatterns = [
    path('addtocart', views.Index.as_view(), name="addtocart"),
    path('mycart', views.Cart.as_view(), name="mycart"),

]
