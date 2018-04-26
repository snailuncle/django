from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View

from .forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from .models import UserProfile,EmailVerifyRecord
from utils.email_send import send_register_email
# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self,username=None,password=None,**kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user 
        except Exception:
            return None

class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")

        
class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    
    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get('email','')
            if UserProfile.objects.filter(email=user_name):
                return render(request,'register.html',{'register_form':register_form,'msg':'用户已存在'})
                
            pass_word=request.POST.get('password','')   
            user_profile=UserProfile()                     
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.is_active=False
            user_profile.password=make_password(pass_word)
            user_profile.save()

            send_register_email(user_name,'register')
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form})

class ForgetPwdView(View):
    def get(self,request):
        forget_form=ForgetForm()        
        return render(request,'forgetpwd.html',{'forget_form':forget_form})
    def post(self,request):
        forget_form=ForgetForm(request.POST)
        if forget_form.is_valid():
            email=request.POST.get('email','')
            send_register_email(email,'forget')
            return render(request,'send_success.html')
        else:
            return render(request,'forgetpwd.html',{'forget_form':forget_form})
            




class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{})
        
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            
            user_name=request.POST.get('username','')
            pass_word=request.POST.get('password','')
            user=authenticate(username=user_name,password=pass_word)
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
                else:
                    return render(request, "login.html", {"msg":"用户未激活！"})                   
            else:
                return render(request,'login.html',{'msg':'用户名或密码错误'})                
        else:    
            return render(request,'login.html',{'login_form':login_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records: 
                email = record.email
                return render(request, "password_reset.html",{'email':email})

        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")

class ModifyPwdView(View):
    """
    修改用户密码
    """
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email, "msg":"密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form})





# def user_login(request):
#     # return HttpResponse('你好')
#     if request.method=='POST':
#         print('请求方式是  %s'%'POST')
#         user_name=request.POST.get('username','')
#         pass_word=request.POST.get('password','')
#         print('用户账号  %s'%user_name)
#         print('用户密码  %s'%pass_word)
#         user=authenticate(username=user_name,password=pass_word)
#         print('验证结果  %s'%str(user))
        
#         if user is not None:
#             print('用户验证通过')
#             login(request,user)
#             return render(request,'index.html')
#         else:
#             print('用户验证失败')        
#             return render(request,'login.html',{'msg':'用户名或密码错误'})
#     elif request.method=='GET':
#         print('请求方式是  %s'%'GET')
        
#         return render(request,'login.html',{})












