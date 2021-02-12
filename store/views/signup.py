from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from store.models.coustomer import Customer
from django.views import View


class signUp(View):

    def validateCustomer(self, customer):
        # form validation
        error_msg = None
        if not customer.first_name:
            error_msg = 'first name required'
        elif len(customer.first_name) < 4:
            error_msg = 'first name must be 4 charactor long'
        elif not customer.last_name:
            error_msg = 'last name required'
        elif len(customer.last_name) < 4:
            error_msg = 'last name must be 4 charactor long'
        elif not customer.phone:
            error_msg = 'phone number required'
        elif len(customer.phone) < 10:
            error_msg = 'phone  must be 10 charactor long'
        elif not customer.last_name:
            error_msg = 'last name required'
        elif len(customer.password) < 6:
            error_msg = 'password must be 6 charactor long'
        elif len(customer.email) < 6:
            error_msg = 'email must be 6 charactor long'
        elif customer.isExist():
            error_msg = 'Email already exist'

        return error_msg

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # values
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_msg = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_msg = self.validateCustomer(customer)

        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_msg,
                'values': value

            }
            return render(request, 'signup.html', data)
