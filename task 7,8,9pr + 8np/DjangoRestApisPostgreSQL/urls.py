"""DjangoRestApisPostgreSQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from customers import views
from users import views as user_views
from orders import views as order_views

urlpatterns = [
    path(r'api/advertisements/', views.advertisement_list.as_view()),
    path(r'api/advertisements/<pk>', views.advertisement_detail.as_view()),
    path(r'api/users/', user_views.RegistrationAPIView.as_view()),
    path(r'api/users/login/', user_views.LoginAPIView.as_view()),
    path(r'api/users/logout/', user_views.LogoutAPIView.as_view()),
    path(r'api/orders/', order_views.Advertisement_OrderViewSet.as_view({'get': 'list', 'post': 'create'})),
    path(r'api/orders/<pk>', order_views.Advertisement_OrderViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
]







