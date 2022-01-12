from django.contrib import admin
from .models import Recipe, RecipeIngredient
from django.contrib.auth.models import User


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    fields = ['name', 'description','unit', 'quantity', 'directions', 'active']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_dispaly = ['name', 'user']
    readonly_fields = ['user', 'created', 'updated']
    raw_id_fields = ['user']



admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)

