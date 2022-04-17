from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from accounts.models import PgOwner, User
from homeapp.models import BookingRooms
from ownerapp.models import Post
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Profile
from profileapp.froms import EditCustomerProfileForm, EditOwnerProfileForm, ProfileNameForm
from projectakash1.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import uuid
from django.conf import settings


# Create your views here.


def profile_view(request):
    posts = Post.objects.all()
    bookings = BookingRooms.objects.all()
    context = {
        'posts':posts,
        'bookings':bookings,
    }
    return render(request, 'profile.html', context)

def showprofile(request):
    posts = Post.objects.all()
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    contact = request.POST.get('contact_no')
    address = request.POST.get('address')
    pro_pic = request.POST.get('pro_pic')

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'contact': contact,
        'address': address,
        'profile': pro_pic,
        'posts': posts,
    }
    return render(request, 'showprofile.html', context)

# class ShowProfile(DetailView):
#     model = User
#     template_name = "showprofile.html"


def password_success(request):
    return render(request, 'password_success.html', )

class PasswordChgnView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url =   reverse_lazy('password_success')

class CustomerProfileEditView(UpdateView):
    form_class = EditCustomerProfileForm
    template_name = "profileedit.html"
    success_url =   reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user.customer

class ProfileNameView(UpdateView):
    form_class = ProfileNameForm
    template_name = "profileedit.html"
    success_url =   reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user


class OwnerProfileEditView(UpdateView):
    form_class = EditOwnerProfileForm
    template_name = "profileedit.html"
    success_url =   reverse_lazy('profile')

    def get_object(self):
        return self.request.user.pgowner





# loginrelated

def ChangePassword(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        if request.method == "POST":
            newpass = request.POST['newpassword']
            confpass = request.POST['confirmpassword']
            user_id = request.POST['user_id']

            if user_id is None:
                messages.success(request, 'Username not found')
                return redirect(f'change_password1/{token}')
            
            if newpass != confpass:
                messages.success(request, 'Password not matched!')
                return redirect(f'change_password1/{token}')
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(newpass)
            user_obj.save()
            return redirect('login')


        context = { 'user_id' : profile_obj.user.id }
    
    except Exception as e:
        print(e)
    return render(request, 'change_password1.html', context)


def ForgetPassword(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            if not User.objects.filter(username = username).first():
                messages.success(request, "Please give correct username")
                return redirect("forget_password")

            user_obj = User.objects.filter(username = username).first()
            token = str(uuid.uuid4())
            profile_obj, created = Profile.objects.get_or_create(user = user_obj)
            print(profile_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, "An email is sent.")
            return redirect("forget_password")

    except Exception as e:
        print(e)
    
    return render(request, 'forgetpassword.html')



def send_forget_password_mail(email, token):
    subject = "Forget Password Link"
    message = f'Your new password is http://127.0.0.1:8000/change_password1/{ token }'
    email_from = EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True




