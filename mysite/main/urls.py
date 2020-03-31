from django.urls import path
from main.views import HomePageView
from . import views

app_name='main' # here for namespacing the urls

urlpatterns = [
	path("", views.login_request, name="login"),
	path("homepage/", HomePageView.as_view(), name="homepage"),
	path("register/", views.register,name="register"),
	path("logout", views.logout_request, name="logout"),
]
