from django.db.models import fields
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from accounts.models import User
from homeapp.models import BookingRooms
from ownerapp.models import ConfirmedBooking, Payment, Post
from django.core.mail import send_mail
from django.conf import settings

from .forms import PostFrom
from django.urls import reverse_lazy
from datetime import datetime


# Create your views here.

# class Home_PostView(CreateView):
#     model = Post
#     form_class = PostFrom
#     template_name = 'postroom.html'

def homepostview(request):
    if request.method == "POST":
        if not request.user.is_owner:
            raise Http404
        else:
            form = PostFrom(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect("/")
    else:
        form = PostFrom(request.POST, request.FILES)
        return render(request, "postroom.html",{'form':form})

def bookingrequests(request):
    bookings = BookingRooms.objects.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'bookedhome.html', context)
        

def confirm_booking(request):
    if request.method == "POST":
        checkin = request.POST['check_in']
        checkout = request.POST['check_out']
        user = get_object_or_404(User, id = request.POST.get('user_id'))
        home_id = get_object_or_404(Post, id = request.POST.get('home_id'))
        home = get_object_or_404(BookingRooms, id = request.POST.get('home_id'))
        con_booking = ConfirmedBooking.objects.create(
            user = home.user,
            room = home_id,
            check_in = str(checkin),
            check_out =  str(checkout),
        )
        con_booking.save()
        message_sub = "Booking Request response."
        booking_msg = "Dear " + home.user.first_name +", Your booking request for " +home.room.home_name+" which owner is "+ user.first_name +" is confirmed. Please contact the owner for further details."
        to_email = home.user.email
        print(to_email)
        send_mail(
                message_sub, # subject
                booking_msg, # message
                settings.EMAIL_HOST_USER, # from email
                [to_email], # To Email
                )
        # obj = get_object_or_404(BookingRooms, id = request.POST.get('home_id'))
        # obj.delete()
        msg = "You've confirmed booking request of " + home.user.first_name + " successfully for the Room "+ home.room.home_name + "from "+checkin+" to " + checkout +"."
        messages.success(request, msg)
        return redirect("/")



class UpdatedpostView(UpdateView):
    model = Post
    template_name = "editpost.html"
    fields = ('home_name','home_image','home_description','room_images1','room_images2','room_images3','PG_type','address', 'price_per_month', 'city','divisions','furniture','AC','fan','bed','light','wifi','parking','breakfast','lunch','dinner')


class DeletepostView(DeleteView):
    model = Post
    template_name = "deletepost.html"
    success_url = reverse_lazy('homepage')