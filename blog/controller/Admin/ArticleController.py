# coding:utf-8
from django.shortcuts import render_to_response, render
from blog.controller.Admin.Controller import Controller
from blog.controller.Admin.LoginController import LoginController

__author__ = 'lenovo'
class ArticleController(Controller):
    def showArticle(self):
        return render(self.request,'admin/Aritcle/showArticles.html')
    def addArticle(self):
        return render(self.request,'admin/Aritcle/addArticle.html')
    def editArticle(self):
        return render(self.request,'admin/Aritcle/editArticle.html')