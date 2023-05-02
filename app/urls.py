from django.urls import path

from . import views

urlpatterns = [
    path("index.html", views.index, name="index"),
    path("cart.html", views.cart, name="cart"),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/<str:action>/<int:cart_id>/', views.change_quantity, name='change_quantity'),
    # path('cart/minus/<int:cart_id>/', views.change_quantity, name='change_quantity'),
    path("clubs.html", views.clubs, name="clubs"),
    path("prices.html", views.prices, name="prices"),
    path("shop.html", views.shop, name="shop"),
    path('profile.html', views.profile, name='profile'),
    path('login-dialog.html', views.login_page, name='login'),

    # path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', views.add_to_cart, name="add_to_cart"),
    # path(r'^order-summary/$', views.order_details, name="order_summary"),
    # path(r'^success/$', views.success, name='purchase_success'),
    # path(r'^item/delete/(?P<item_id>[-\w]+)/$', views.delete_from_cart, name='delete_item'),
    # path(r'^checkout/$', views.checkout, name='checkout'),
    # path(r'^update-transaction/(?P<token>[-\w]+)/$', views.update_transaction_records, name='update_records')
]