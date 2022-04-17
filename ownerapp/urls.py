from django.urls.conf import path
from . import views

urlpatterns = [
    # path('rooms', views.Home_PostView.as_view(), name='rooms'),
    path('rooms', views.homepostview, name='rooms'),
    path('details/edit/<int:pk>', views.UpdatedpostView.as_view(), name="update_post"),
    path('details/<int:pk>/remove', views.DeletepostView.as_view(), name="delete_post"),
    path('bookingrequests', views.bookingrequests, name="bookingrequests"),
    path('confirmbooking', views.confirm_booking, name="confirmbooking"),
    
]