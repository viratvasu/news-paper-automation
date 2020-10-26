from django.contrib import admin
from .models import UserProfile,Subscription
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Subscription)