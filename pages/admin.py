from django.contrib import admin
from . models import users
from . models import matchmaking
from . models import training
from . models import lobby

# Register your models here.

admin.site.register(users)
admin.site.register(matchmaking)
admin.site.register(training)
admin.site.register(lobby)
