from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from accounts.models import PgOwner, User
from ownerapp.models import Post
# Create your views here.

def searcheditems(request):
    if request.method == 'POST':
        div = request.POST['search_division']
        city = request.POST['search_city']
        searched = True
        if div == "" and city =="":
            messages.success(request, "Searchbar is Empty")
            return redirect('homepage')
        
        else:
            if city == "":
                post = Post.objects.filter(divisions__icontains = div)
                context = {
                'searched': searched,
                'posts': post,
                }
                return render(request, 'searchitems.html',context)
            else:
                post = Post.objects.filter(divisions__icontains = div, city__icontains = city)
                context = {
                    'searched': searched,
                    'posts': post,
                }
                return render(request, 'searchitems.html',context)
    