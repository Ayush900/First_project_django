from django.urls import path
from . import views
app_name='apptwo'
urlpatterns = [
path('',views.index,name='index'),
]
