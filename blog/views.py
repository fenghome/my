# coding:utf-8
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from blog.controller.Admin.LoginController import LoginController

from blog.models import Users


def admin(request,controller,action):
    # 先检查是否已经登录，如果没有登录，调用LoginController的login方法
    if request.session.get('username') is None:
        c = LoginController(request)
        return c.login()
    # 根据传进来的控制器和操作动态调用相应的controller
    exec 'from blog.controller.Admin.'+controller+'Controller import '+controller+'Controller'
    exec 'c = '+controller+'Controller(request)'
    exec 'res = c.'+action+'()'
    return res

