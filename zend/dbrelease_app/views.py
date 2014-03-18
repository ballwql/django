from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from forms import LoginForm,ChangepwdForm,CreatetaskForm
import datetime
from .models import *
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('dbrelease_app/login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('dbrelease_app/index.html', RequestContext(request))
            else:
                return render_to_response('dbrelease_app/login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('dbrelease_app/login.html', RequestContext(request, {'form': form,}))
@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/accounts/login/")
@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render_to_response('dbrelease_app/changepwd.html', RequestContext(request, {'form': form,}))
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('dbrelease_app/index.html', RequestContext(request,{'changepwd_success':True}))
            else:
                return render_to_response('dbrelease_app/changepwd.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))
        else:
            return render_to_response('dbrelease_app/changepwd.html', RequestContext(request, {'form': form,}))
@login_required
def tasklist(request):
    username=request.user.username
    if len(Dba.objects.filter(username=username)) == 0: #User is not DBA, only shows his/her own tasklist
        userid=User.objects.filter(username=username)
        lines = Task.objects.filter(creater=userid).order_by("-id")
    else:   #User is DBA, shows all tasklist
        lines = Task.objects.order_by("-id")
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('dbrelease_app/tasklist.html', RequestContext(request, {'lines': show_lines,}))
@login_required
def createtask(request):
    if request.method == 'GET':
        form = CreatetaskForm(initial={
        'creater':request.user.last_name + request.user.first_name,
        })
        return render_to_response('dbrelease_app/createtask.html', RequestContext(request, {'form': form,}))
    else:
        form = CreatetaskForm(request.POST,request.FILES)
        if form.is_valid():
            username = request.user.username
            t = Task.objects.create(
                creater = User.objects.get(username=username),
                manager = form.cleaned_data['manager'],
                dba = Dba.objects.get(id=1),
                state = State.objects.get(statename='Open'),
                sql = form.cleaned_data['sql'],
                desc = form.cleaned_data['desc'],
                createdtime = datetime.datetime.now(),
                lastupdatedtime = datetime.datetime.now(),
                attachment = form.cleaned_data['attachment'],
            )
            databaselist = form.cleaned_data['databases']
            for db in databaselist:
                t.databases.add(db)
            t.save()
            return render_to_response('base.html', RequestContext(request,{'createtask_success':True,}))
        else:
            return render_to_response('dbrelease_app/createtask.html', RequestContext(request, {'form':form,}))