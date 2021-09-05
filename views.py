from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Customer, Cart, OrderPlaced


def orders(request):
  """
    This method is used to display order page of request for order
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a page of request for product for oder page which is a HTML page.
    For adding to to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
  op = OrderPlaced.objects.filter(user=request.user)
  return render(request, 'app/orders.html', {'order_placed':op})


def checkout(request):
    """
    This method is used to display a checkout request for payment
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a payment page of request for product checkout which is a HTML page.
    For adding to to cart user must be logged into his/her account.
    :rtype: HttpResponse.
    """
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 80.0  
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
      for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
      totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

