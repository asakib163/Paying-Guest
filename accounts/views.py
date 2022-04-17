from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from accounts.froms import CustomerSignUpForm, PgOwnerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from accounts.models import User, Customer, PgOwner

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def register(request):
    return render(request, 'register.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")
    context={
        'form': AuthenticationForm(),
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'creg.html'
    def validation(self, form):
        user = form.save()
        login(self.request.user)
        return redirect('login')

class PgOwner_register(CreateView):
    model = User
    form_class = PgOwnerSignUpForm
    template_name = "oreg.html"
    def validation(self, form):
        user = form.save()
        login(self.request.user)
        return redirect('/')
    
