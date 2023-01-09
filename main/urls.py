from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile/<str:pk>', views.profile, name='profile'),

    path('clients', views.clients, name="clients"),
    path('client/update/<str:pk>', views.client_update, name="clientupdate"),
    path('client/delete/<str:pk>', views.client_delete, name="clientdelete"),

    path('bills/ongoing', views.ongoing_bills, name="ongoingbills"),
    path('bills/history', views.history_bills, name="billshistory"),
    path('bill/update/<str:pk>', views.update_bills, name="billupdate"),
    path('bill/delete/<str:pk>', views.delete_bills, name="billdelete"),

    path('users', views.users, name="users"),
    path('user/update/<str:pk>', views.update_user, name="updateuser"),
    path('user/delete/<str:pk>', views.delete_user, name="deleteuser"),

    path('metrics', views.metrics, name="metrics"),
    path('metrics/update/<str:pk>', views.metricsupdate, name="metricsupdate")

    
]
