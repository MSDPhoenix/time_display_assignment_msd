from django.shortcuts import render, HttpResponse
from time import gmtime,strftime,localtime

def time_display(request):
    context = {
        'date':strftime("%b %d, %Y",localtime()),  #HOW DO I CHANGE THIS TO LOCAL TIME INSTEAD OF GW TIME????
        "time1": strftime("%H:%M %p",localtime()),
        "time2": strftime("%H:%M %p",gmtime()),
        "time3": strftime("%H:%M %p"),
    }
    return render(request,'time_display.html',context)

