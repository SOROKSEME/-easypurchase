from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from .models import Category, Product
from .forms import LoginForm, RegistrationForm

# Create your views here.


class HomeListView(ListView):
    model = Product
    context_object_name = "item"
    template_name = "pages/index.html"


class SearchResult(HomeListView):
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(
            title__icontains=query
        )


def shop_view(request):
    product = Product.objects.all()
    context = {
        "product": product
    }
    return render(request, "pages/shop.html", context)


def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    product = Product.objects.filter(category=category)
    context = {
        "product": product
    }

    return render(request, "pages/shop.html", context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        "product": product
    }
    return render(request, "pages/details_product.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "pages/login.html", context)


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    context = {
        "form": form
    }
    return render(request, "pages/registration.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


class SearchResults(HomeListView):
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(
            title__iregex=query
        )
