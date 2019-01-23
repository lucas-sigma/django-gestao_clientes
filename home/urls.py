from django.urls import path
from .views import home, my_logout

urlpatterns = [
    path('', home),
    path('logout/', my_logout, name='my_logout')
]