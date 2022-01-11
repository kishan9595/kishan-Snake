from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog/<str:id>/', views.blog, name='blog'),
    
    path('create-article/', views.createArticle, name='create-article'),
    path('update-article/<int:id>/', views.updateArticle, name='update-article'),
    path('delete-article/<int:id>/', views.deleteArticle, name='delete-article'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
# path('search/', views.search_view, name='search'),