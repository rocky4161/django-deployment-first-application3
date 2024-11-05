from django.shortcuts import render

# Create your views here.
def students1(request):
    return render(request,'SecondApp/students1.html');


def students2(request):
    return render(request, 'SecondApp/students2.html');

import datetime
def wishes2(request):
    date1=datetime.datetime.now()
    msg1='Hello User/Client...GOOD';
    hr=int(date1.strftime('%H'));
    if hr<12:
        msg1+=' Morning!!'
    elif hr<16:
        msg1+=' Afternoon!!'
    elif hr<20:
        msg1+=' Evening!!'
    else:
        msg1='Hello User/Client...Very Good Night!!'
    dict1={'date1':date1,'msg1':msg1}
    return render(request,'FirstApp/wishes2.html',context=dict1);
