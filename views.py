from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Product, Cart
from django.db.models import Q
from django.http import JsonResponse
"""
Global Variables

"""

def add_to_cart(request):
    """
    This method is used to display Cart page of request for Add to cart.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page of request for product add to cart which is a HTML page.
    For adding to to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
    user=request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    """
    This method is used to display Cart page of request for Add to cart.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page of request for product add to cart which is a HTML page.
    For adding to to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        user=request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request,'app/emptycart.html')
            
def plus_cart(request):
    """
    This method is used to add more product into cart.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page of request for product add more product to cart which is a HTML page.
    For adding to to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
    if request.method == "GET":
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      c.quantity+=1
      c.save()
      amount = 0.0
      shipping_amount = 80.0
      cart_product = [p for p in Cart.objects.all() if p.user == request.user]
      for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
           
      data ={
        'quantity': c.quantity,
        'amount':amount,
        'totalamount':amount + shipping_amount
        }
      return JsonResponse(data)

def minus_cart(request):
    """
    This method is used to decrement more product from cart.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page of request for decrementing product from cart which is a HTML page.
    For access to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
    if request.method == "GET":
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      c.quantity-=1
      c.save()
      amount = 0.0
      shipping_amount = 80.0
      cart_product = [p for p in Cart.objects.all() if p.user == request.user]
      for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
           
      data ={
        'quantity': c.quantity,
        'amount':amount,
        'totalamount':amount + shipping_amount
        }
      return JsonResponse(data)

def remove_cart(request):
    """
    This method is used to remove cart permanently
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page with a empty cart picture which is a HTML page.
    For access to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
    if request.method == "GET":
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      c.delete()
      amount = 0.0
      shipping_amount = 80.0
      cart_product = [p for p in Cart.objects.all() if p.user == request.user]
      for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
           
      data ={
        'amount':amount,
        'totalamount':amount + shipping_amount
        }
      return JsonResponse(data)


















