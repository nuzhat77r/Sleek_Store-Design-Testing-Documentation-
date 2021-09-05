from django.contrib.auth.models import user
from django.shortcuts import render
from django.views import View
from .models import Customer
from .forms import  CustomerProfileForm
from django.contrib import messages

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(Self,request):
     """
    This method is used to decrement more product from cart.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page of request for decrementing product from cart which is a HTML page.
    For access to cart user must be logged into his/her account.
    :rtype: HttpResponse.
     """
    form = CustomerProfileForm(request.POST)
      if form.is_valid():
        usr = request.user
        name = form.cleaned_data['name']
        locality = form.cleaned_data['locality']
        city = form.cleaned_data['city']
        zipcode = form.cleaned_data['zipcode']
        division = form.cleaned_data['division']
        reg = Customer(user=usr, name=name, locality=locality, city=city, zipcode=zipcode, division=division)
        reg.save()
        messages.success(request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

