# coding:utf-8
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from blog.controller.Admin.Controller import Controller
from blog.models import Users

__author__ = 'Administrator'
class UserController(Controller):
    def addUser(self):
        if self.request.method == 'POST':
            username = self.request.POST['username']
            userpass = self.request.POST['userpass']
            userrepass = self.request.POST['userrepass']
            if username == '':
                return render(self.request,'admin/User/addUser.html',{'note':'用户名不能为空'})
            elif userpass == '':
                return render(self.request,'admin/User/addUser.html',{'note':'密码不能为空'})
            elif Users.objects.filter(username = username).exists() is True:
                return render(self.request,'admin/User/addUser.html',{'note':'用户名已存在'})
            elif userpass != userrepass :
                return render(self.request,'admin/User/addUser.html',{'note':'两次输入的密码不一致'})

            Users(username=username,userpassword = userpass).save()
            return HttpResponseRedirect(reverse('ht', args=('User','showUser')))

        else:
            return render(self.request,'admin/User/addUser.html')


    def editUser(self):
        if self.request.method == 'POST':
            username = self.request.POST.get('username')
            userpass = self.request.POST.get('userpass')
            oldname = self.request.POST.get('oldname')
            print oldname
            user = Users.objects.filter(username = username)
            if username == '':
                return render(self.request,'admin/User/editUser.html',{'username':username,'userpass':userpass,'note':'用户名不能为空'})
            elif userpass == '':
                return render(self.request,'admin/User/editUser.html',{'username':username,'userpass':userpass,'note':'密码不能为空'})
            elif user.exists() is True:
                return render(self.request,'admin/User/editUser.html',{'username':username,'userpass':userpass,'note':'用户名已存在'})
        #     更新用户名
            newuser = Users.objects.get(username = oldname)
            newuser.username = username
            newuser.userpassword = userpass
            newuser.save()
            # return HttpResponseRedirect(reverse('ht', args=('User','showUser')))
            #或者用下面的方方法
            return self.showUser()

        else:
            username = self.request.GET.get('username')
            userpass = Users.objects.get(username = username).userpassword
            return render(self.request,'admin/User/editUser.html',{'username':username,'userpass':userpass})

    def showUser(self):
        usersList = Users.objects.all()
        return render(self.request,'admin/User/showUser.html',{'usersList':usersList})

    def delUser(self):
        username = self.request.GET.get('username')

        return HttpResponse(username)