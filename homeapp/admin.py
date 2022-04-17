from xml.etree.ElementTree import Comment
from django.contrib import admin

from homeapp.models import BookingRooms, House_Comment


# Register your models here.
admin.site.register(BookingRooms)
admin.site.register(House_Comment)