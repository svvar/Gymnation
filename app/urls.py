from django.urls import path

from . import views

urlpatterns = [
    path("index.html", views.index, name="index"),
    path("cart.html", views.cart, name="cart"),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/<str:action>/<int:cart_id>/', views.change_quantity, name='change_quantity'),
    path("clubs.html", views.clubs, name="clubs"),
    path("prices.html", views.prices, name="prices"),
    path("shop.html", views.shop, name="shop"),
    path('profile.html', views.profile, name='profile'),
    path('login-dialog.html', views.login_page, name='login'),

]