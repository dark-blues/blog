from django.shortcuts import render

# Create your views here.
#注册视图
from django.views import View


class RegisterView(View):
    """用户注册"""
    def get(self,request):
        return render(request,'register.html')