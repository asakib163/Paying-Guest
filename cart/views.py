from django.shortcuts import redirect, render
from django.views import View
from ownerapp.models import Post
# Create your views here.
class Index(View):
    def post(self, request):
        home = request.POST.get('home_id')
        remove = request.POST.get('removecart')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(home)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(home)
                    else:
                        cart[home] = quantity-1
                else:
                    cart[home] = quantity+1
            else:
                cart[home] = 1

        else:
            cart = {}
            cart[home] = 1
        request.session['cart'] = cart
        print('cart',request.session['cart'])
        return redirect('details/'+home)
    def get(self, request):
        cart =  request.session.get('cart')
        if not cart:
            request.session['cart'] = {}


class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Post.objects.filter(id__in =ids)
        print(products)
        return render(request , 'cart_view.html' , {'posts' : products} )