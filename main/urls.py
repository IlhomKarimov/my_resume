from django.urls import path
from .views import ContactView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact')
]