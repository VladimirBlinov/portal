from django.urls import path

from mortgage import views


urlpatterns = [
    path('', views.index, name='mortgage'),
]
