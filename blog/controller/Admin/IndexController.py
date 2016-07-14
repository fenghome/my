# coding:utf-8
from django.shortcuts import render_to_response

__author__ = 'Administrator'
class IndexController:
    def index(self):
        return render_to_response('Admin/index/index.html')
    def head(self):
        return render_to_response('Admin/index/head.html')
    def left(self):
        return render_to_response('Admin/index/left.html')
    def right(self):
        return render_to_response('Admin/index/right.html')