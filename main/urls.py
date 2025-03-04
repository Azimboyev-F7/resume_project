from django.urls import path
from .views import index, index2

app_name = 'orbit'

urlpatterns = [
    path('index/', index, name='index'),
    path('', index2, name='index-2'),
]

