from time import strftime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from dayoff.form import Dayoffform
from dayoff.models import Profile


def my_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user.groups.filter(name='Manager').exists():
            login(request, user)
            return redirect("/admin/")
        elif user.is_superuser==0:
            login(request, user)
            return redirect("formoff")
        else:
            context['username'] = username
            context['password'] = password


    return render(request, template_name='login.html', context=context)

@login_required
def formoff(request):
    form_user = Dayoffform()
    if request.method == "POST":
        form_user = Dayoffform(request.POST)
        if form_user.is_valid():
            id = request.user.id
            user = User.objects.get(id=id)
            dayoff = Profile.objects.create(reason=form_user.cleaned_data.get("reason"),
                                            type=form_user.cleaned_data.get("type"),
                                            date_start=form_user.cleaned_data.get("startdate"),
                                            date_end=form_user.cleaned_data.get("enddate"),
                                            approve_status='รอการอณุมัติ',
                                            user_id=user.id)

            return redirect('formoff')
    context = {
        'form': form_user,
    }
    return render(request, 'formoff.html', context=context)

@login_required
def status(request):
    id = request.user.id
    status = list(Profile.objects.filter(user_id=id).values())
    stat = []
    for i in status:
        stat.append({'id': i['id'], 'user_id': i['user_id'], 'reason': i['reason'], 'type': i['type'],
                     'date_start': i['date_start'].strftime('%Y-%m-%d'), 'date_end': i['date_end'].strftime('%Y-%m-%d'),
                     'approve_status': i['approve_status']})
    context = {
        'stat': stat
    }
    return render(request, 'status.html', context=context)

def my_logout(requset):
	logout(requset)
	return redirect('login')