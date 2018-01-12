# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import (
    View, 
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)
from django.urls import reverse



from taskmanager.models import Task, Group
from taskmanager.forms import TaskForm, LoginForm
import json


def my_view(request):
    task_count = Task.objects.all().count()
    return HttpResponse(
        json.dumps({"count": task_count})
    )


class MyView(View):
    def get(self, request, *args, **kwargs):
        task_count = Task.objects.all().count()
        return render(
            request, 
            'my-view-template.html',
            context={'no_tasks': task_count}
        )


class MyTemplateView(TemplateView):
    template_name = 'my-view-template_name.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(MyTemplateView, self).get_context_data(*args, **kwargs)
        context['no_tasks'] = Task.objects.all().count()
        return context
        

class GroupListView(ListView):
    template_name = 'home.html'
    model = Group
    context_object_name = 'groups'
    
    def get_queryset(self, *args, **kwargs):
        return Group.objects.filter(public=True)
    
    
class GroupDetailView(LoginRequiredMixin, DetailView):
    template_name = 'group.html'
    model = Group
    context_object_name = 'group'
    

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'task.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = TaskForm
    model = Task
    
    def get_success_url(self, *args, **kwargs):
        return reverse(
            'task_detail', 
            kwargs={
                'pk': self.object.pk
            }
        )


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = TaskForm
    model = Task
    
    def get_success_url(self, *args, **kwargs):
        return reverse(
            'task_detail', 
            kwargs={
                'pk': self.object.pk
            }
        )


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Task
    
    def get_success_url(self, *args, **kwargs):
        return reverse(
            'group_detail', 
            kwargs={
                'pk': self.object.group.pk
            }
        )


def login_view(request):
    context = {}
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('group_list')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
