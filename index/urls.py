from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about', views.about),
    path('contacts', views.contacts),
    path('category/<int:pk>', views.get_exact_category),
    path('product/<int:pk>', views.get_exact_product),
    path('search', views.search_product),
    path('cart', views.user_cart),
    path('del-item/<int:pk>', views.del_from_cart),
    path('add-to-cart/<int:pk>', views.add_to_cart),
]
