from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_views, name = "index"),
    path('edit/<int:id>/', views.edit_topic, name='edit_topic'),
    path('delete/<int:id>/', views.delete_topic, name='delete_topic'),
]