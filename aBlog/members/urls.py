from django.urls import path
from .views import UserRegistrationView, UserEditView, ChangePasswords, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
# allows us to use some of the views that come with the authentication system that comes with django
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="registrationPage"),
    path('edit-settings/', UserEditView.as_view(), name="editSettingsPage"),

    # the argument in PasswordChangeView.as_view removes the django admin theme
    # path("password/", auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"), name="password")
    path("password/", ChangePasswords.as_view(
        template_name="registration/change-password.html"), name="password"),
    # redirecting password change to a specific page
    path('password-success/', views.password_success, name="password_success"),

    path("<int:pk>/profile/", ShowProfilePageView.as_view(), name="profiles"),
    path("<int:pk>/edit_profile_page/", EditProfilePageView.as_view(), name="profile_page"),
    path("create_profile_page/",CreateProfilePageView.as_view(), name="create_profile_page"),
]
