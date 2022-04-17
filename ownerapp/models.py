from django.db import models
from django.urls import reverse

from accounts.models import PgOwner, User
# Create your models here.
class Post(models.Model):
    CHOICES =(
            ("Yes", "Yes"), 
            ("No", "No"), 
            )
    DIVISIONS = (
            ("CTG", "Chittagong"),
            ("DHA", "Dhaka"),
            ("RAJ", "Rajshahi"),
            ("MYM", "Mymensingh"),
            ("RAN", "Rangpur"),
            ("SYL", "Sylhet"),
            ("KHU", "Khulna"),
            ("BAR", "Barishal"),
        )
    
    PG_TYPE = (
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Both', 'Both')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    home_name = models.CharField(max_length=50)
    home_image = models.ImageField(upload_to="Home/Home_Images")
    room_images1 = models.ImageField(upload_to="Home/Room_Images1")
    room_images2 = models.ImageField(upload_to="Home/Room_Images2")
    room_images3 = models.ImageField(upload_to="Home/Room_Images3")
    home_description = models.TextField(default="This is a beautiful house", max_length=100)
    post_date = models.DateField(auto_now_add=True)
    PG_type = models.CharField(max_length=50, choices=PG_TYPE, default= 'Both')
    address = models.CharField(max_length=300)
    price_per_month = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    divisions = models.CharField(max_length=100, choices=DIVISIONS)
    furniture = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    AC = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    fan = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    bed = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    light = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    wifi = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    parking = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    breakfast = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    lunch = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    dinner = models.CharField(max_length=10,choices = CHOICES, default = 'Yes')
    like = models.ManyToManyField(User, related_name= "blog_posts", blank = True)
    
    
    def total_likes(self):
        return self.like.count()
        
    def __str__(self):
        return self.home_name + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('homepage')

    
    
class ConfirmedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Post, on_delete=models.CASCADE)
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.user}, {self.room} '

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.CharField(max_length=50)

    def __str__(self):
        return f'Paid {self.payment}  By {self.user} '
