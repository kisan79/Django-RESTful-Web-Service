from django.shortcuts import render
from django.http import HttpResponse
import json

# Creating function-Based-View For Giving a HttpResponse which taking Html-Response
def htmlResponseView(request):
    emp_details={
        'Name':'Kisan',
        'Age':23,
        'Id':101,
        'isJoined':False,
        'Stream':'Developer',
        'Join-date':'27-06-2020'
    }
    htmlRes='<h1 style="color:darkcyan;">ename:{}<br>Age:{}<br>empno:{}<br>isjoined ?{}<br>Stream:{}<br>Join-date:{}</h1>'.format(emp_details['Name'],emp_details['Age'],emp_details['Id'],emp_details['isJoined'],emp_details['Stream'],emp_details['Join-date'])
    return HttpResponse(htmlRes)

# Creating function-Based-View For Giving a HttpResponse which give JSON-Response

def JSONResponseView(request):
    emp_details={
        'Name':'Kisan',
        'Age':23,
        'Id':101,
        'isJoined':False,
        'Stream':'Developer',
        'Join-date':'27-06-2020'
    }
    #Converting our Python dict object
    JSONRes=json.dumps(emp_details,indent=0)
    print(JSONRes)
    return HttpResponse(JSONRes)


# Creating function-Based-View For Giving a HttpResponse which give JSON-Response that contains many objects

def JSONResponseView2(request):
    emp_details=[
        {
        'Name':'Kisan',
        'Age':23,
        'Id':101,
        'isJoined':False,
        'Stream':'Developer',
        'Join-date':'27-06-2020'
    },
    {
        'Name':'Kumar',
        'Age':24,
        'Id':102,
        'isJoined':True,
        'Stream':'Tester',
        'Join-date':'28-06-2020'
    },
    {
        'Name':'Shitu',
        'Age':22,
        'Id':103,
        'isJoined':True,
        'Stream':'Manager',
        'Join-date':'27-06-2020'
    }
    ]
    #Converting our Python dict object
    JSONRes=json.dumps(emp_details,indent=0)
    print(JSONRes)
    return HttpResponse(JSONRes)
