from django.shortcuts import render
from django.http import HttpResponse

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
