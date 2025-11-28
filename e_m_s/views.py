from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
# Create your views here.
file_name="ems/static/emps.json"
def read_data():
    with open(file_name,"r") as f:
         return json.load(f)
def write_data(data):
    with open(file_name,'w') as f:
         json.dump(data,f)

def emp_adding_form(request):
    return render(request,"emp.html")
# @post view
@api_view(["POST"])
def creating_Emp(request):
    data=request.POST.dict()
    # return HttpResponse("hello")
    # print(data,"form data in post req")
    datafromJSONFile=read_data()
    datafromJSONFile["employees"].append(data)
    write_data(datafromJSONFile)
    # print(datafromJSONFile,"data from json")
    return HttpResponse("emp add successfully")