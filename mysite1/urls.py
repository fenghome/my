"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.blog,name='Blog'),
    url(r'^admin/(\S+)/(\S+)/$', views.admin,name='ht'),



    # url(r'^login/', views.login,name='login'),

#     url(r'^head/', views.head,name='ht_head'),
#     url(r'^left/', views.left,name='ht_left'),
#     url(r'^right/', views.right,name='ht_right'),
#     url(r'^showUser/', views.showUser,name='ht_showUser'),
#     url(r'^showColumn/', views.showColumn,name='ht_showColumn'),
#     url(r'^showArticles/', views.showArticles,name='ht_showArticles'),
#     url(r'^addUser/', views.addUser,name='ht_addUser'),
#     url(r'^editPass/', views.editPass,name='ht_editPass'),
#     url(r'^addColumn/', views.addColumn,name='ht_addColumn'),
#     url(r'^addArticle/', views.addArticle,name='ht_addArticle'),
#     url(r'^editUser/', views.editUser,name='ht_editUser'),
#     url(r'^editColumn/', views.editColumn,name='ht_editColumn'),
#     url(r'^editArticle/', views.editArticle,name='ht_editArticle'),
#     url(r'^admin/(\d+)/(\d+)/$',views.admin,name='add'),
]
