"""
URL configuration for AugustaCRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.index,name = "Home"),
    path('empty-newleads/',views.EmptyNewLeads,name = "empty new leads"),
    path('empty-call-list/',views.EmptyCallList,name = "empty call list"),

    path('services/',views.services, name = "services"),
    path('services/call-leads/',views.CallLeads, name = "call-leads"),
    path('services/call-leads/new-leads/',views.NewLeads, name = "call-leads"),
    # new leads log processing
    path('services/call-leads/new-calendly/',views.Newcalendly, name = "new-calendly"),
    path('services/call-leads/new-callback/',views.NewCallBack),
    path('services/call-leads/new-notanswred/',views.NewNotAnswred),
    path('services/call-leads/new-notintrested/',views.NewNotIntrested),
    path('services/call-leads/new-Invalid/',views.NewInvalid),


    path('services/call-leads/call-list/',views.CallList, name = "call-list"),
    # processing url
    path('services/call-leads/call/',views.Call),
    # result log processing
    # path('services/call-leads/call-result/',views.CallResult, name = "call-result"),
    path('services/call-leads/calendly/',views.calendly, name = "calendly"),
    # path('services/call-leads/result-log/',views.ResultLog, name = "call-result-log"),
    path('services/call-leads/result-log/call-back/',views.CallBackLater),
    path('services/call-leads/result-log/not-answered/',views.NotAnswered),
    path('services/call-leads/result-log/not-intrested/',views.NotIntrested),
    path('services/call-leads/result-log/invalid/',views.Invalid),

    

    
     
]
