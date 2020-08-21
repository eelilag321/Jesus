from django.urls import path
from . import views
from .views import PrayerCreateView, PrayerListView

urlpatterns = [
    path('', views.index, name='index'),
    path('pray/', PrayerCreateView.as_view(), name='pray'),
    path('prayer-list/', PrayerListView.as_view(), name='list'),
    path('about-jesus-criest/', views.about, name='about')
]