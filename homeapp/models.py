from django.db import models
from django.forms import TextInput
from accounts.models import User
from ownerapp.models import Post
import datetime

# Create your models here.

class BookingRooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Post, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f' {self.user}, {self.room} '

class House_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(default=0)
    cmnt_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


