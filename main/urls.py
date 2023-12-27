from django.urls import path

from main import views

app_name = "main"

# namespace 'main'

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("about-us/", views.AboutPage.as_view(), name="about_page"),
]
