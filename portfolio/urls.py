from django.urls import path

from . import views

urlpatterns = [
    # path('', views.links, name='links'),
    # path('hello_world', views.hello_world, name='hello_world'),
    path('', views.portfolio, name='portfolio'),
    path('thanks', views.thanks, name='thanks'),
]
