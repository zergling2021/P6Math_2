from django.urls import path

from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#]
from . import views
app_name = 'science'

urlpatterns = [
    path('', views.index, name='index'),
]