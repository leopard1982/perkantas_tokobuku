from django.urls import path
from adminpage.views import welcome

urlpatterns = [
    path('', welcome,name='welcome')
] 