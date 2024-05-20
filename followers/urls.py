from django.urls import path
from followers import views

path('followers', 'view.FollowersList.as_view'()),
path('followers/ < int:pk > /', views.FollowerDetail.as_view())