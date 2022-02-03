from . import views
from django.urls import path

urlpatterns = [
    path("login",views.login),
    path("registration",views.registration),
    path("register",views.register),
    path("fetch_login",views.fetch_login),
    # path("profile",views.profile),
    # path("edit",views.edit),
    # path("update",views.update),
    path("contact",views.contact),
    path("logout",views.logout),





]
