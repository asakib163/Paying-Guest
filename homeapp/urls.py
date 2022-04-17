from django.urls.conf import path
from homeapp import views

urlpatterns = [
    path('', views.home_page.as_view(), name='homepage'),
    path('homepage', views.home_page.as_view(), name='homepage'),
    path('payment_list', views.PaymentListView.as_view(), name='payment_list'),
    path('details/<int:pk>', views.Home_DetailView.as_view(), name='details'),
    path('like/<int:pk>', views.LikeView , name="like_post"),
    path('bookingroom', views.bookingroom , name="bookingroom"),
    path('cancelbooking', views.cancelbooking , name="cancelbooking"),
    path('make_payment', views.make_payment, name= "make_payment"),
    path('comment', views.comments, name= "comment"),

]