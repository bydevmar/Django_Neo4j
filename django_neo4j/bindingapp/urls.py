from django.urls import path
from . import views

urlpatterns = [
    path('create_person/', views.create_person, name='create_person'),
    path('get_person/<str:name>/', views.get_person, name='get_person'),
    path('update_person/<str:name>/', views.update_person, name='update_person'),
    path('delete_person/<str:name>/', views.delete_person, name='delete_person'),
]   