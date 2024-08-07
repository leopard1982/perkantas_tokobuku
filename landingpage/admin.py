from django.contrib import admin
from landingpage.models import customerDb, customerBook, customerBookmark
# Register your models here.

admin.site.register(customerDb)
admin.site.register(customerBook)
admin.site.register(customerBookmark)