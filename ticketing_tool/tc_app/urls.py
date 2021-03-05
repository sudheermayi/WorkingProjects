from django.urls import path

from .views import configure
urlpatterns = [path('tc_tool/', configure, name='configure')]