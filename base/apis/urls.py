from django.urls import path


from .views import SponsorPreferenceList, SponsorPreferenceDetail

urlpatterns = [
    path("", SponsorPreferenceList.as_view()),
    path("<int:pk>/", SponsorPreferenceDetail.as_view()),
]