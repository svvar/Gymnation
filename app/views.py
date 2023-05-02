from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from app.models import Products
from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .accounts.forms import RegisterForm
from .accounts.models import GymUser
from .models import Cart

def index(request):
    if request.user.is_authenticated:
        print("user here")
    return render(request, "index.html")

def clubs(request):
    return render(request, "clubs.html")


def prices(request):
    return render(request, "prices.html")

def get_all_filter_values(category:str):
    manufacturers = set()
    tastes = dict()
    p_types = set()

    products = Products.objects.filter(category=category)

    for p in products:
        if p.manufacturer not in manufacturers:
            manufacturers.add(p.manufacturer)

        for taste in p.tastes:
            if taste not in tastes:
                tastes.update({taste: p.tastes[taste]})

        if p.p_type not in p_types:
            p_types.add(p.p_type)


    manufacturers = sorted(manufacturers)
    tastes = dict(sorted(tastes.items(), key=lambda item: item[1]))
    p_types = sorted(p_types)

    return {'manufacturers': manufacturers, 'tastes': tastes, 'p_types': p_types}

def shop(request):
    taste = request.POST.get("tastes")
    print(taste)


    category = request.GET.get("category")
    manufacturers = request.GET.getlist('manufacturer')
    tastes = request.GET.getlist('taste')
    p_types = request.GET.getlist('type')

    page_number = request.GET.get('page')

    if category is None:
        category = "protein"

    try:
        if manufacturers[0]:
            manufact_query = Q()
            for m in manufacturers[0].split(","):
                manufact_query |= Q(manufacturer=m)

        if tastes[0]:
            tastes_query = Q()
            for t in tastes[0].split(","):
                tastes_query &= Q(tastes=t)

        if p_types[0]:
            types_query = Q()
            for t in p_types[0].split(","):
                types_query |= Q(p_type=t)

    except IndexError:
        pass

    filter_query = Q(category=category)
    try:
        filter_query &= manufact_query
    except NameError:
        pass

    try:
        filter_query &= tastes_query
    except NameError:
        pass

    try:
        filter_query &= types_query
    except NameError:
        pass

    # Get the products that match the filter query
    products = Products.objects.filter(filter_query)

    pages = Paginator(products, 8)
    page_obj = pages.get_page(page_number)

    context = {'products': products} | get_all_filter_values(category) | {'selected_category': category} | {'user': request.user}
    print(request.user.is_authenticated)
    return render(request, "shop.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        if request.POST.get("action") == "logout":
            logout(request)
            return redirect("shop.html")


    context = {'user': request.user}
    print(context)
    return render(request, 'profile.html', context)

def login_page(request):
    if request.method == "POST":
        if request.POST.get("action") == "login":

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, "login-dialog.html", {'login_error': True})

        if request.POST.get("action") == "signup":
            form = RegisterForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data.get('firstname')
                last_name = form.cleaned_data.get('lastname')
                phone = form.cleaned_data.get('phone')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = GymUser.objects.create_user(first_name, last_name, phone, email, password)
                user.save()

                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect('profile')
            else:
                errors = [e for e in form.errors.values()]
                context = {"signup_error": errors}
                return render(request, "login-dialog.html", context)

    return render(request, "login-dialog.html")



@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    print(cart_items)
    cart_total_value = 0
    for item in cart_items:
        item.product = Products.objects.get(id=item.product_id)
        cart_total_value += item.total()

    context = {'cart_items': cart_items, 'cart_total': cart_total_value}
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, product_id):
    selected_taste = request.GET.get("selected_taste")
    print(selected_taste)


    product = Products.objects.get(id=product_id)
    cart_item = Cart(user=request.user, product=product, taste=selected_taste, price=product.price, quantity=1)
    cart_item.save()
    messages.success(request, f"{product.name} added to cart")
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, f"{cart_item.product.name} removed from cart")
    else:
        messages.error(request, "You don't have permission to remove this item from the cart.")
    return redirect('cart')

@login_required
def change_quantity(request, action, cart_id):
    print(action)

    cart_item = Cart.objects.get(id=cart_id)
    if action == "plus":
        cart_item.quantity += 1
    elif action == "minus" and cart_item.quantity >= 2:
        cart_item.quantity -= 1

    cart_item.save()
    return redirect('cart')
