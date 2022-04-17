from django import template

register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(post, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == post.id:
            return True
    return False

@register.filter(name = 'cart_count')
def cart_count(post, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == post.id:
            return cart.get(id)
    return 0
