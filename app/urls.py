from django.urls import path

from . import views

urlpatterns = [
    path("index.html", views.index, name="index"),
    # ex: /app/5/
    path("cart.html", views.cart, name="cart"),
    # ex: /app/5/results/
    path("clubs.html", views.clubs, name="clubs"),
    # ex: /app/5/vote/
    path("prices.html", views.prices, name="prices"),
    path("shop.html", views.shop, name="shop"),
    path("test.html", views.test, name="test"),
    path('profile.html', views.profile, name='profile'),
    path('login-dialog.html', views.login_page, name='login')
    # path('login-dialog.html', views.login, name='login'),
    # path('register/', views.register, name='register'),
]