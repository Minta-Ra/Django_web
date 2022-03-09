# record_store urls

from django.urls import path

from . import views

urlpatterns = [
    # This will happen going to /inventory
    path("", views.index, name='index')
]