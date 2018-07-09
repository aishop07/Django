"""firstclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from member import views
from products import views

router = DefaultRouter()
router.register(r'members', views.MemberViewSet)
router_drinks = DefaultRouter()
router_drinks.register(r'drinks', views.DrinksViewSet)
router_foods = DefaultRouter()
router_foods.register(r'foods', views.FoodsViewSet)
router_orders = DefaultRouter()
router_orders.register(r'orders', views.OrdersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('member/',include('member.urls')),
    path('products/',include('products.urls')),
    path('api/', include(router_drinks.urls)),
    path('api/', include(router_foods.urls)),
    path('api/', include(router_orders.urls)),
    path('api/', include(router.urls))
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
