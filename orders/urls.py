from django.urls import path
from orders import views


urlpatterns = [
    path("",views.index, name='index')
]