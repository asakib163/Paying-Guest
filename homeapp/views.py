from django.contrib import messages
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import View
from accounts.models import User
from homeapp.models import BookingRooms,  House_Comment
from ownerapp.models import Payment, Post
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail

from homeapp.booking_functions.availability import availability
from datetime import datetime

from django.conf import settings


# Create your views here.

class home_page(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-post_date']


class Home_DetailView(DetailView):
    model = Post
    template_name = 'details_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home_DetailView, self).get_context_data()
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        comment = House_Comment.objects.filter(post = self.kwargs['pk'])
        liked = False
        if stuff.like.filter(id = self.request.user.id).exists():
            liked =True

        context['total_likes'] = total_likes
        context['liked'] = liked
        context['comments'] = comment
        return context
        

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))


def bookingroom(request):
    if request.method == "POST":
        checkin = request.POST['check_in']
        checkout = request.POST['check_out']
        user = get_object_or_404(User, id = request.POST.get('user_id'))
        home = get_object_or_404(Post, id = request.POST.get('home_id'))
        check_in = datetime.strptime(checkin, '%Y-%m-%d').date()
        check_out = datetime.strptime(checkout, '%Y-%m-%d').date()
        print(user.email)
        
        booking = BookingRooms.objects.create(
            user = user,
            room = home,
            check_in = check_in,
            check_out =  check_out,
        )
        booking.save()
        message_sub = "Booking Request response."
        booking_msg = "Dear " + user.first_name +", Your request for " +home.home_name +" has been accepted. The Owner will contact with you sortly."
        to_email = user.email
        print(to_email)
        send_mail(
                message_sub, # subject
                booking_msg, # message
                settings.EMAIL_HOST_USER, # from email
                [to_email], # To Email
                )
        msg = "You've requested successfully for the Room from "+checkin+" to " + checkout +". Please check your email for confirmation."
        messages.success(request, msg)
        return redirect("/")
    

def cancelbooking(request):
    if request.method == "POST":
        home = request.POST['home_id']
        user = request.POST['user_id']
        checkin = request.POST['check_in']
        checkout = request.POST['check_out']
        user_id = get_object_or_404(User, id = request.POST.get('user_id'))
        obj = get_object_or_404(BookingRooms, id = request.POST.get('home_id'))
        obj.delete()
        messages.success(request, 'The booking is canceled')
        return redirect("profile")


def make_payment(request):
    if request.method == "POST":
        payment = request.POST['payment']
        user = get_object_or_404(User, id = request.POST.get('user_id'))
        owner = get_object_or_404(User, id = request.POST.get('owner_id'))
        pay = (int(payment) *20)/ 100
        print(user)
        print(owner.first_name)
        con_payment = Payment.objects.create(
            user = user,
            payment = str(pay)
        )
        con_payment.save()
        message_sub = "Payment confirmation."
        booking_msg = "Dear " + owner.first_name +", Your customer "+user.first_name+ " paid the advance."
        to_email = owner.email
        send_mail(
                message_sub, # subject
                booking_msg, # message
                settings.EMAIL_HOST_USER, # from email
                [to_email], # To Email
                )

        return redirect("/")
    
        
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment.html'


def comments(request):
    if request.method == "POST":
        user = get_object_or_404(User, id = request.POST.get('user_id'))
        post = get_object_or_404(Post, id = request.POST.get('post_id'))
        rate = request.POST['rate']
        cmnt = request.POST['comment_input']
        post_id = request.POST['post_id']
        print(int(rate))
        post_idst =  (int(post_id))
        
        commnet = House_Comment.objects.create(
            user = user,
            post = post,
            rate = int(rate),
            comment = cmnt,
        )
        commnet.save()
        return redirect("details/"+str(post_idst))