from django.urls import path
from . import views
from .views import destination


urlpatterns = [
        path("register/", views.register, name='register'),
        path("login", views.login, name="login"),
        path("logout", views.logout, name = "logout"),
        path('destination/<int:pk>/', destination, name = "destination")
    ]