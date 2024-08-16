from django.contrib import admin
from landingpage.models import customerDb, customerBook, customerBookmark
# Register your models here.

class viewCustomerDb(admin.ModelAdmin):
    list_display= ('username','id_customer','alias','birthday')

admin.site.register(customerDb,viewCustomerDb)
admin.site.register(customerBook)
admin.site.register(customerBookmark)