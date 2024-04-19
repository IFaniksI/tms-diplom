from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Gym)
admin.site.register(Trainer)
admin.site.register(Service)
admin.site.register(Subscription)
