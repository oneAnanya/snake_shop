from django.contrib import admin
from .models import Snake, Bin
# Register your models here.


class SnakeAdmin(admin.ModelAdmin):
    list_display = ("name","price","color")

class BinAdmin(admin.ModelAdmin):
    list_display = ( "name","price","shape")


admin.site.register(Snake,SnakeAdmin)
admin.site.register(Bin,BinAdmin)
