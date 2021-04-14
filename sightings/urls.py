from django.urls import path

from . import views

app_name='sightings'

urlpatterns = [
    path('',views.index),
    path('info/', views.all_squirrels,name='info'),
    path('map/',views.map),
    path('add/', views.add),
    path('stats/',views.statistics),
    path('<Unique_squirrel_id>/', views.update_squirrel),
]
