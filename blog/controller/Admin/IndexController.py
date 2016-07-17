# coding:utf-8
from django.shortcuts import render_to_response, render
from blog.controller.Admin.Controller import Controller
from blog.controller.Admin.LoginController import LoginController

__author__ = 'Administrator'
class IndexController(Controller):
    def index(self):
        return render(self.request,'admin/index/index.html')
    def head(self):
        username = self.request.session.get('username')
        return render(self.request,'admin/index/head.html',{'username':username})
    def left(self):
        return render(self.request,'admin/index/left.html')
    def right(self):
        return render(self.request,'admin/index/right.html')
