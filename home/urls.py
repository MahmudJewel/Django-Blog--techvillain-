from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home_view, name='home'),
]
