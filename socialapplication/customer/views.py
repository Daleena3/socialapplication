from django.shortcuts import render,redirect
from customer.forms import RegistrationForm,LoginForm,ProfileForm,UserProfileForm
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from customer.models import UserProfile
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout,signin
# Create your views here.

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signup")
        else:
            return render(request,"signup.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})
        else:
            return render(request,"login.html",{"form":form})

class IndexView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")


class CreateProfileView(View):

     def get(self,request,*args, **kwargs):
        qs=UserProfile.objects.filter(user=request.user)
        return render(request,"profile-detail.html",{"profile":qs})
     
class ProfileUpdateView(View):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile-edit.html"
    success_url=reverse_lazy("profile-detail")
    pk_url_kwarg="id"

class ProfileDeletelView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ques=UserProfile.objects.get(id=id).delete()
        return redirect("indext")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



             