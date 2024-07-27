from django.urls import path
from landingpage.views import welcome
urlpatterns = [
    path('', welcome,name='welcome')
] 