from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views import signup,login
from .views.login import logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('',Index.as_view(),name="homepage"),
    path('signup',signup.signUp.as_view() , name='signup'),
    path('login',login.login.as_view(), name='login'),
    path('logout',logout, name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('check-out',auth_middleware(CheckOut.as_view()), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
