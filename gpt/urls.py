from django.urls import path
from .views import UsernameView


urlpatterns = [
    path('generate/', UsernameView.as_view())
]

