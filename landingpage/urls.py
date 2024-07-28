from django.urls import path
from landingpage.views import welcome, testPDF

urlpatterns = [
    path('', welcome,name='welcome'),
    path('test/',testPDF,name="testPDF")
] 