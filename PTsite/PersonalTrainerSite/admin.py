from django.contrib import admin
from .models import Trainer, Client
# Register your models here.

# this give me access to modifying data through admin page
admin.site.register(Trainer)
admin.site.register(Client)

# this makes it easier to hard code data