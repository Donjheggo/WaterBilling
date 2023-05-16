from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from account.models import *
from .forms import *
from django.db.models import F
import sweetify
from account.forms import *
from main.decorators import *
import datetime
from twilio.rest import Client as TwilClient

def landingpage(request):
    return render(request, 'landingpage/landingpage.html')  


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'clients': Client.objects.all().count(),
        'bills': WaterBill.objects.all().count(),
        'ongoingbills': WaterBill.objects.filter(status='Pending'),
        'connecteds': Client.objects.filter(status='Connected').count(),
        'disconnecteds': Client.objects.filter(status='Disconnected').count(),
    }
    return render(request, 'main/dashboard.html', context)

@login_required(login_url='login')
@verified_or_superuser
def ongoing_bills(request):
    context = {
        'title': 'Ongoing Bills',
        'ongoingbills': WaterBill.objects.filter(status='Pending'),
        'form': BillForm()
    }
    if request.method == 'POST':
        try: 
            billform = BillForm(request.POST)
            if billform.is_valid():
                billform.save()
                sweetify.toast(request, 'Successfully Added.')
                return HttpResponseRedirect(request.path_info)
        except:
            sweetify.toast(request, 'Invalid Details', icon='error')
        try: 
            number = request.POST['contact_number']
            totalbill = request.POST['total_bill']
            duedate = request.POST['due_date']
            penaltydate = request.POST['penalty_date']
            SID = 'AC21815705abea7ed84796f7a14a9ae178'
            Auth_Token = 'dda90e1a2a24f16b143220aa883d34c2'
            sender = '+17262005435'
            receiver = number
            message = f'\n Your Total Bill is: {totalbill} pesos \n\n Your due date is: {duedate} \n\n Your penalty date is: {penaltydate}'
            cl = TwilClient(SID, Auth_Token)
            cl.messages.create(body=message, from_=sender, to=receiver)
            sweetify.toast(request, 'Notification Sent')
        except:
            sweetify.toast(request, 'Contact Number is invalid format', icon='error')
    return render(request, 'main/billsongoing.html', context)


@login_required(login_url='login')
@verified_or_superuser
def history_bills(request):
    context = {
        'title': 'Bills History',
        'billshistory': WaterBill.objects.filter(status='Paid'),
        'form': BillForm()
    }
    return render(request, 'main/billshistory.html', context)

@user_passes_test(lambda u: u.is_superuser)
def update_bills(request, pk):
    bill = WaterBill.objects.get(id=pk)
    form = BillForm(instance=bill)
    context = {
        'title': 'Update Bill',
        'bill': bill,
        'form': form,
    }
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            sweetify.toast(request, f'{bill} updated successfully.')
            return HttpResponseRedirect(reverse('ongoingbills'))
    return render(request, 'main/billupdate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_bills(request, pk):
    bill = WaterBill.objects.get(id=pk)
    context = {
        'title': 'Delete Bill',
        'bill': bill,
    }
    if request.method == 'POST':
        bill.delete()
        sweetify.toast(request, f'{bill} deleted successfully.')
        return HttpResponseRedirect(reverse('ongoingbills'))
    return render(request, 'main/billdelete.html', context)



@login_required(login_url='login')
@verified_or_superuser
def profile(request, pk):
    profile = Account.objects.get(id=pk)
    student_form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        student_form = UpdateProfileForm(request.POST, instance=profile)
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 != password2:
            print("password does not match")
            sweetify.error(request, 'Password does not match!')
            return HttpResponseRedirect(request.path_info)
        elif student_form.is_valid():
            student_form.save()
            sweetify.success(request, 'Updated Successfully')
            return HttpResponseRedirect(reverse('login'))
        else: 
            sweetify.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(request.path_info)
    context = {
        'title': 'Profile',
        'student_form': student_form,
        'profile': profile,
    }
    return render(request, 'main/profile.html', context)

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    context = {
        'title': 'Users',
        'users': Account.objects.filter(is_superuser=False)
    }
    return render(request, 'main/users.html', context)

@user_passes_test(lambda u: u.is_superuser)
def update_user(request, pk):
    user = Account.objects.get(id=pk)
    form = UpdateUserForm(instance=user)
    context = {
        'title': 'Users',
        'user': user,
        'form': form,
    }
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            sweetify.toast(request, f'{user} updated sucessfuly')
            return HttpResponseRedirect(reverse('users'))
    return render(request, 'main/userupdate.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, pk):
    user = Account.objects.get(id=pk)
    context = {
        'title': 'Users',
        'user': user,
    }
    if request.method == 'POST':
        user.delete()
        sweetify.toast(request, 'Deleted successfuly.')
        return HttpResponseRedirect(reverse('users'))
    return render(request, 'main/userdelete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def clients(request):
    form = ClientForm()
    context = {
        'title': 'Clients',
        'clients': Client.objects.all(),
        'form': form
    }
    if request.method == 'POST':
        form = ClientForm(request.POST)
        contact_number = request.POST['contact_number']
        check_number = Client.objects.filter(contact_number=contact_number).exists()
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Client added')
            return HttpResponseRedirect(reverse('clients'))
        elif check_number:
            sweetify.toast(request,'Phone number already exist', icon='error')
        else:
            sweetify.toast(request, 'Invalid details', icon='error')
    return render(request, 'main/clients.html', context)

@user_passes_test(lambda u: u.is_superuser)
def client_update(request,pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    context = {
        'title': 'Update Client',
        'client': client,
        'form': form
    }
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Client updated successfully')
            return HttpResponseRedirect(reverse('clients'))
        else:
            sweetify.toast(request, 'Invalid Details', icon='error')
    return render(request, 'main/clientupdate.html', context)


@user_passes_test(lambda u: u.is_superuser)
def client_delete(request,pk):
    client = Client.objects.get(id=pk)
    context = {
        'title': 'Delete Client',
        'client': client,
    }
    if request.method == 'POST':
        client.delete()
        sweetify.toast(request, 'Client deleted successfully')
        return HttpResponseRedirect(reverse('clients'))
    return render(request, 'main/clientdelete.html', context)



def metrics(request):
    if not Metric.objects.all():
        Metric.objects.create()
    context = {
        'title': 'Metrics',
        'amount': Metric.objects.get(id=1)
    }
    return render(request, 'main/metrics.html', context)



def metricsupdate(request, pk):
    metrics = Metric.objects.get(id=pk)
    form = MetricsForm(instance=metrics)
    context = {
        'title': 'Update Metrics',
        'form': form
    }
    if request.method == 'POST':
        form = MetricsForm(request.POST, instance=metrics)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Metrics updated successfully')
            return HttpResponseRedirect(reverse('metrics'))
    return render(request, 'main/metricsupdate.html', context)
