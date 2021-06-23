from django.urls import path, include
from .views import *

urlpatterns = [
    path('', employee_form, name='employee_form'),
    path('<int:id>/', employee_form, name='employee_update'),
    path('delete/<int:id>/', employee_delete, name='employee_delete'),
    path('list/', employee_list, name='employee_list'),
]
