from django.urls import path
from .views import persons_list, persons_create, persons_update, persons_delete

urlpatterns = [
    path('lista/', persons_list, name='persons_list'),
    path('novo/', persons_create, name='persons_new'),
    path('update/<int:id>', persons_update, name='persons_update'),
    path('delete/<int:id>', persons_delete, name='persons_delete')
]