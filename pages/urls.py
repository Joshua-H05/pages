from django.urls import path
from .views import HomePageView, AboutView, RandomPage
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name="about"),
    path("random/", RandomPage.as_view(), name="random"),
]
