# coding:utf-8
from django.shortcuts import render_to_response, render
from blog.controller.Admin.Controller import Controller
from blog.controller.Admin.LoginController import LoginController

__author__ = 'lenovo'
class ColumnController(Controller):
    def showColumn(self):
        return render(self.request,'admin/Column/showColumn.html')
    def editColumn(self):
        return render(self.request,'admin/Column/showColumn.html')
    def addColumn(self):
        return render(self.request,'admin/Column/showColumn.html')