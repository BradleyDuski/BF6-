from django.contrib import admin
from .models import Operator, Post, Reply, Like, Weapon
# Register your models here.
admin.site.register(Operator)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Weapon)