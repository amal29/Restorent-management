from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from . forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import json
from .models import *
import datetime
import pytz
from HotelBooking.settings import EMAIL_HOST_USER
from django.core.mail import send_mail






def Register(request):
    context={}
    if request.POST:
        print("reg users", request.POST)
        form=UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print("validdddddddd")
            form.save()
            return redirect('login')
        context['register_form']=form 
    else:
        form=UserRegistrationForm()
        context['register_form']=form 

        
    return render(request,"auth/signup.html",context)



def login_view(request):
    context={}
    if request.POST:
        form=UserLoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            print(user)

            if user is not None:
                login(request,user)
                return redirect("rhome")

        else:
            context['login_form']=form

        
    else:
        form=UserLoginForm()
        print(form)
        context['login_form']=form

    return render(request,'auth/login.html',context)  




def logout_view(request):
     logout(request)
     return redirect("/")   










def Home(request):
    context={}
    room=Room.objects.all()
    context={"room":room}
    return render(request,'index.html',context)






def Rhome(request):
    context={}
    room=Room.objects.all()
    user=request.user.username

    ob=MyUser.objects.filter(username=user)

    context={"room":room,"ob":ob}

    return render(request,'registeredindex.html',context)



def BookingView(request):
    data=dict()
    if request.POST:
        fromJs = request.POST
        print(fromJs)
        d1=fromJs["d1"]
        d2=fromJs["d2"]
        user=request.user.username
        print("aazzzzz",user)
        d1= datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M').replace(tzinfo=pytz.UTC)
        d2= datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M').replace(tzinfo=pytz.UTC)
        print("date1",type(d1))
        print("date2",type(d2))
        b=Booking.objects.filter(room=fromJs["BookId"])
        for j in b:
            print("j.check_in",j.check_in)
            print("Type-check_in",type(j.check_in))
            if (d1 > j.check_out) and (d2 > j.check_in):
                print("aa")
                Booking.objects.create(user=user, room=fromJs["BookId"],check_in=d1,check_out=d2,image=fromJs["imgdata"])
                subject = 'SunRise Room Booking'
                message = 'Your Room is Booked Successfully'
                recepient = request.user.email
                print("recepient",recepient)
                send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                data['submited']= True


            else:
                data['submited']= False
    

        if Booking.objects.filter(room=fromJs["BookId"]).count() == 0:
                Booking.objects.create(user=user, room=fromJs["BookId"],check_in=d1,check_out=d2,image=fromJs["imgdata"])
                subject = 'SunRise Room Booking'
                message = 'Your Room is Booked Successfully'
                recepient = request.user.email
                print("recepient",recepient)
                send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                data['submited']= True

    room=request.GET.get("BookId")
    r=Room.objects.filter(name=room)
    context={"r":r}
    data['html_form']= render_to_string('book.html',context,request=request)
    return JsonResponse(data)



def Myroom(request):
    data=dict()
    b=Booking.objects.all()
    context={"b":b}
    data['html_form']= render_to_string('myroom.html',context,request=request)
    return JsonResponse(data)

def DeleteRoom(request):
    data=dict()
    if request.POST:
       print(request.POST)
       roomID=request.POST.get("roomid")
       room= Booking.objects.filter(pk=roomID)

       room.delete()
       b=Booking.objects.all()
       context={"b":b}
       data['html_form']= render_to_string('myroom.html',context,request=request)
    return JsonResponse(data)




