"""
URL configuration for cafeSaas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from orders.views import create_order, view_orders
from users.views import login_view, registration_view
from logs.views import logs_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waiter/', create_order, name='waiter'),
    path('orders/', view_orders, name='orders'),
    path('login/', login_view, name='login'),
    path('', login_view, name='index_login'),
    path('reg/', registration_view, name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logs/', logs_view, name='admin')
]
