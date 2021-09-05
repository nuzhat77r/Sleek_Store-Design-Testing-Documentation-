from django.shortcuts import render
from django.views import View
from .models import Product
def women(request, data=None):
    """
    This method is used to display home page of request for covid test service online.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a home page of request for covid test service online which is a HTML page if
    the user is logged in. else it will return the log in page.
    """
    if data == None:
      women = Product.objects.filter(category='W')
    elif data == 'Saree' or data== 'Salwar-Kameez':
      women = Product.objects.filter(category="W").filter(brand=data)
    elif data == 'below':
      women = Product.objects.filter(category="W").filter(discounted_price__lt=2500)
    elif data == 'above':
       women = Product.objects.filter(category="W").filter(discounted_price__gt=2500)
    return render(request, 'app/women.html', {'women':women})
