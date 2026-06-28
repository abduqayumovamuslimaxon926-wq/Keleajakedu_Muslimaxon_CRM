from django.shortcuts import render
from .models import Student, Group  # Group modelini ham chaqirib oldik

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'crm_main/student_list.html', {'students': students})

# Yangi guruhlar funksiyasi:
def group_list_view(request):
    groups = Group.objects.all()
    return render(request, 'crm_main/group_list.html', {'groups': groups})