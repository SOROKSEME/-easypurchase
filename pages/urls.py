from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("shop/", views.shop_view, name="shop"),
    path("shop/categories/<slug:slug>/", views.category_products, name="category_products"),
    path("shop/products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("search/", views.SearchResult.as_view(), name="search"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/registration", views.registration_view, name="registration"),
    path("accounts/logout", views.user_logout, name="logout"),
    path("search/", views.SearchResults.as_view(), name="search"),
]
