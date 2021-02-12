from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.coustomer import Customer
from django.views import View

class login(View):

    return_url=None

    def get(self,request):
        login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_Email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id



                if login.return_url:
                    return HttpResponseRedirect(login.return_url)
                else:
                    login.return_url=None
                    return redirect('homepage')
            else:
                error_msg = 'email or password invalid'
        else:
            error_msg = 'email or password invalid'
        return render(request, 'login.html', {'error': error_msg})


def logout(request):
    request.session.clear()

    return redirect('login')