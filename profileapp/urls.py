
from django.urls.conf import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile', views.profile_view, name='profile'),
    path('showprofile', views.showprofile, name='showprofile'),
    path('profile/editname/<int:pk>', views.ProfileNameView.as_view(), name='editname'),
    path('profile/edit1/<int:pk>', views.CustomerProfileEditView.as_view(), name='editprofile1'),
    path('profile/edit/<int:pk>', views.OwnerProfileEditView.as_view(), name='editprofile'),
    path('profile/password/', views.PasswordChgnView.as_view(template_name = "change_password.html")),
    path('password_success', views.password_success, name = 'password_success'),
    path('forget_password', views.ForgetPassword, name = 'forget_password'),
    path('change_password1/<token>', views.ChangePassword, name = 'change_password1'),
    #path('profile/password/', auth_views.PasswordChangeView.as_view(template_name = "change_password.html")),
]
