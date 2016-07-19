# coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.controller.Admin.Controller import Controller
from blog.models import Users

__author__ = 'Administrator'

class LoginController(Controller):
    def login(self):
            if self.request.method == 'POST':
                username = self.request.POST['username']
                password = self.request.POST['userpass']
                rs = Users.objects.filter(username = username)
                if rs.exists() is False:
                    return render(self.request,'admin/Login/login.html',{'tishi':'用户名不存在'})
                elif rs[0].userpassword != password:
                    return render(self.request,'admin/Login/login.html',{'tishi':'输入的密码错误'})
                else:
                    self.request.session['username'] = username
                    self.request.session['password'] = password
                    # return HttpResponseRedirect(reverse('ht', args=('Index','index')))
                    return render(self.request,'admin/Index/index.html')
            else:
                return render(self.request,'admin/Login/login.html')

    def logout(self):
        del self.request.session['username']
        return render(self.request,'admin/Login/login.html')