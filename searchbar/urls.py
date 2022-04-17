
from django.urls.conf import path
from . import views

urlpatterns = [
    path('searcheditems',views.searcheditems, name='searcheditems'),
]
