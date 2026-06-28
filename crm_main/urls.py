from django.urls import path
from .views import student_list_view, group_list_view

urlpatterns = [
    path('', student_list_view, name='home'), # Asosiy manzilga kirganda student_list_view ochiladi
    path('students/', student_list_view, name='student_list'),
    path('groups/', group_list_view, name='group_list'),
]