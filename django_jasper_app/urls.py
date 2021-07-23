from django.urls import path
from . import views
app_name = 'django_jasper_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('entries/', views.entries, name='entries'),
]