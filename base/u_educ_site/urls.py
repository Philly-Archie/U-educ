from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path("signup/", views.signup, name="signup"),
    path('', views.home, name='home'),

    path('profile/', views.profile, name='profile'),
    path('mappings/', views.mappings, name='mappings'),
    path('donations/', views.donations, name='donations'),
    path('sponsor_preferences/', views.sponsorPreferences, name='sponsor_preferences'),



    # path("reset_password/", auth_views.PasswordResetView.as_view(
    #    template_name="auth/reset_password.html"), name="reset_password"),

    # path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(
    #     template_name="auth/password_sent.html"), name="password_reset_done"),

    # path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
    #     template_name="auth/confirm_password.html"), name="password_reset_confirm"),

    # path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(
    #     template_name="auth/password_complete.html"), name="password_rest_complete"),
]