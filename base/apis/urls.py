from django.urls import path


from .views import SponsorPreferenceList, SponsorPreferenceDetail
from .import views

urlpatterns = [
    path("", SponsorPreferenceList.as_view()),
    path("<int:pk>/", SponsorPreferenceDetail.as_view()),
    path('create_user/', views.create_user, name='create_user'),
    path('create_details/', views.create_details, name='create_details'),
    path('create_fam_education/', views.create_fam_education, name='create_fam_education'),

]