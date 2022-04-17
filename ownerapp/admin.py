from django.contrib import admin

from ownerapp.models import ConfirmedBooking, Payment, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(ConfirmedBooking)
admin.site.register(Payment)