from django.urls import path

from users import views

app_name = "users"

# namespace 'users'

urlpatterns = [
    path("profile/", views.ProfilePage.as_view(), name="profile"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.LogoutPage.as_view(), name="logout"),
    path("registration/", views.RegistrationPage.as_view(), name="registration"),
]
