# coding:utf-8
from django.http.response import HttpResponse

from django.shortcuts import render_to_response, render

__author__ = 'lenovo'
class LoginController:
    def __init__(self,request):
        self.request = request
    def login(self):
        if self.request.method == 'POST':
            print 'post'
            return render(self.request,'admin/Index/index.html')
        else:
            print 'no post'
            return render(self.request,'admin/Login/login.html')

