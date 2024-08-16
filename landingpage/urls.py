from django.urls import path
from landingpage.views import welcome, testPDF, test2

urlpatterns = [
    path('', welcome,name='welcome2'),
    path('test/',testPDF,name="testPDF"),
    path('test2/<str:test>',test2,name="test2")
] 