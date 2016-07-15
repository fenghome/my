# coding:utf-8
from django.shortcuts import render_to_response, render
from blog.controller.Admin.LoginController import LoginController

__author__ = 'Administrator'
class UserController(LoginController):
    def addUser(self):
       return render(self.request,'admin/User/addUser.html')
    def editUser(self):
       return render(self.request,'admin/User/editUser.html')
    def showUser(self):
       return render(self.request,'admin/User/showUser.html')