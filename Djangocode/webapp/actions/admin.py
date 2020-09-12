from django.contrib import admin
from .models import Car
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id','Company','Model','Color','Date','Price','Engine_capacity','Number_plate','Seating_capacity')
