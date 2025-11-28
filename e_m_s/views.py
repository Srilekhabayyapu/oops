from django.shortcuts import render

# Create your views here.
def emp_adding_form(request):
    return render(request,"emp.html")