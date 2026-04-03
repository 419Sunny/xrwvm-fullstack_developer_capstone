from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [CarModelInline]


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'year', 'model_type')
    list_filter = ('car_make', 'model_type', 'year')
    search_fields = ('name',)


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
