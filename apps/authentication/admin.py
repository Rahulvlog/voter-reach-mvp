

from django.contrib import admin
from .models import Profile, State, District, City
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "address", "phone"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)