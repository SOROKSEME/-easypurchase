from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("to_cart/<int:product_id>/<str:action>/", views.to_cart, name="to_cart"),
    path("payment/", views.create_checkout_session, name="payment"),
    path("payment/success/", views.success_payment, name="success_payment")
]

