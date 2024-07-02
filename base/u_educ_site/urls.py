from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path("signup/", views.signup, name="signup"),
    path('', views.home, name='home'),

    path('profile/', views.profile, name='profile'),
    path('mappings/', views.mappings, name='mappings'),
    path('map_requests/', views.mapRequests, name='map_requests'),
    path('sponsor_preferences/', views.sponsorPreferences, name='sponsor_preferences'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
    path('add_student/<str:pk>/', views.addStudent, name='add_student'),
    path('delete_map_request/<str:pk>/', views.deleteMapRequest, name='delete_map_request'),
    path('end_mapping/<str:pk>/', views.endMapping, name='end_mapping'),


    # Admin urls
    path('admin_dashboard/', views.adminDashboard, name='admin_dashboard'),
    path('view_sponsor_details/<str:pk>/', views.viewSponsor, name='admin_view_sponsor'),
    path('view_student_details/<str:pk>/', views.viewStudent, name='admin_view_student'),
    path('admin_mappings/', views.mappings, name='admin_mappings'),
    path('admin_map_requests/', views.mapRequests, name='admin_map_requests'),



    # path("reset_password/", auth_views.PasswordResetView.as_view(
    #    template_name="auth/reset_password.html"), name="reset_password"),

    # path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(
    #     template_name="auth/password_sent.html"), name="password_reset_done"),

    # path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
    #     template_name="auth/confirm_password.html"), name="password_reset_confirm"),

    # path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(
    #     template_name="auth/password_complete.html"), name="password_rest_complete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)