from django.urls import path
from .views import emp_adding_form,creating_Emp
urlpatterns=[
    path("",emp_adding_form),
    path("api/emp/create/",creating_Emp,name="creating_emp")
]