"""
Registration View documentation
------------------------------------------

"""

from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
"""
Code Packages for registration

"""

      
class CustomerRegistrationView(View):
    """
    This class is extended from the View class so it has all the functionality
    of the view class.
    this class used to create objects 
    """
    
    def get(self, request):
        """
        This method is used to show the regisration form by clicking one of the option it shows the corresponding registration page.
        :param request: it's a HttpResponse from user.
        :type request: HttpResponse.
        :return: render the basic view of registration.html for customer of clothing store.It returns a html page where it has username,email,password,address form to proceed for registration.
        :rtype: HttpResponse.
        """
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
        

    def post(self, request):
        """
        This method is used to show confirmation after registration.After registration it post a message on the screen confirming that 
        registarion is successfull.If any of the data from the box is missing while registration for it post a message that all box 
        need to fillup
        :param request: it's a HttpResponse from user.
        :type request: HttpResponse.
        :return: this method render a html page.It returns a page where it has two retun type.
        One is successfull and another is fill all box to complete register
        :rtype: HttpResponse.
        """
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})
        







