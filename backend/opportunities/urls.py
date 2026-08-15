from django.urls import path
from .views import opportunities_list

urlpatterns = [
    path("", opportunities_list, name="opportunities-list")
]