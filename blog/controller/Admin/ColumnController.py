# coding:utf-8
from django.shortcuts import render_to_response, render
from blog.controller.Admin.Controller import Controller
from blog.controller.Admin.LoginController import LoginController
from blog.models import Columns

__author__ = 'lenovo'
class ColumnController(Controller):
    #显示栏目
    def showColumn(self):
        columns = Columns.objects.all()
        return render(self.request,'admin/Column/showColumn.html',{'columns':columns})

    #编辑栏目
    def editColumn(self):
        if self.request.method == 'POST':
            oldColName = self.request.POST.get('oldName')
            newColName = self.request.POST.get('colName').strip()
            if newColName == '':
                return render(self.request,'admin/Column/editColumn.html',{'note':'栏目名称不能为空'})
            elif Columns.objects.filter(colname = newColName).exists() is True:
                return render(self.request,'admin/Column/editColumn.html',{'note':'栏目已经存在','colName':newColName})

            #没有以上问题更新栏目
            colModel = Columns.objects.get(colname = oldColName)
            colModel.colname = newColName
            colModel.save()
            return self.showColumn()
        else:
            inColName = self.request.GET.get('colName')
            return render(self.request,'admin/Column/editColumn.html',{'colName':inColName})

    #增加栏目
    def addColumn(self):
        if self.request.method == 'POST':
            inColName = self.request.POST.get('colName').strip()
            if inColName == '':
                return render(self.request,'admin/Column/addColumn.html',{'note':'栏目名称不能为空'})
            elif Columns.objects.filter(colname = inColName).exists() is True:
                return render(self.request,'admin/Column/addColumn.html',{'note':'栏目名称已经存在'})
            Columns(colname = inColName).save()
            return self.showColumn()
        else:
            return render(self.request,'admin/Column/addColumn.html')

    #删除栏目
    def delColumn(self):
        colName = self.request.GET.get('colName')
        Columns.objects.get(colname = colName).delete()
        return self.showColumn()