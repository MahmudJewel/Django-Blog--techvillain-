from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog/<int:pk>', views.category_view, name='blog'),
    path('search', views.search_view, name='search')
]
