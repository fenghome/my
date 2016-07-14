# coding:utf-8
from django.shortcuts import render_to_response

__author__ = 'Administrator'
class UserController:
    def addUser(self):
       return render_to_response('Admin/User/addUser.html')
    def editUser(self):
       return render_to_response('Admin/User/editUser.html')
    def showUser(self):
       return render_to_response('Admin/User/showUser.html')