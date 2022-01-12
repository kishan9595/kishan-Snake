from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list_view, name='list'),
    path('create/', views.recipe_create_view, name='create'),
    path('<int:id>/change/', views.recipe_update_view, name='update'),
    path('<int:id>/', views.recipe_detail_view, name='detail'),
]