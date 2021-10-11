from django.shortcuts import render
from time import strftime
from pytz import timezone
from datetime import datetime

def time_display(request):
    context = {
        "date1":datetime.now(timezone('Asia/Taipei')).strftime("%b %d, %Y"),
        "time1":datetime.now(timezone('Asia/Taipei')).strftime("%H:%M %p"),
        "date2":datetime.now(timezone('America/New_York')).strftime("%b %d, %Y"),
        "time2":datetime.now(timezone('America/New_York')).strftime("%H:%M %p"),
        "date3":datetime.now(timezone('America/Chicago')).strftime("%b %d, %Y"),
        "time3":datetime.now(timezone('America/Chicago')).strftime("%H:%M %p"),
        "date4":datetime.now(timezone('America/Los_Angeles')).strftime("%b %d, %Y"),
        "time4":datetime.now(timezone('America/Los_Angeles')).strftime("%H:%M %p"),
    }
    return render(request,'time_display.html',context)

