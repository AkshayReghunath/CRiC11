from django.contrib import admin

# Register your models here.
from .models import Player, Bat, Bowl, BallType, BatType,Team

admin.site.register(Player)
admin.site.register(Bat)
admin.site.register(Bowl)
admin.site.register(BallType)
admin.site.register(BatType)
admin.site.register(Team)