from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout ,name='checkout'),
]
