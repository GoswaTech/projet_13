from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_library/', views.my_library, name='my_library'),
    path('my_likes/', views.my_likes, name='my_likes'),
    path('living_room/<int:user_id>/', views.living_room, name='living_room'),
]
