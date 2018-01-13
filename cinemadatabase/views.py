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



from cinemadatabase.models import Film,Actor,Discussion
from cinemadatabase.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import json


def my_view(request):
    film_count = Film.objects.all().count()
    return HttpResponse(
        json.dumps({"count": film_count})
    )


class MyView(View):
    def get(self, request, *args, **kwargs):
        film_count = Film.objects.all().count()
        return render(
            request, 
            'my-view-template.html',
            context={'no_films': film_count}
        )


class MyTemplateView(TemplateView):
    template_name = 'my-view-template_name.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(MyTemplateView, self).get_context_data(*args, **kwargs)
        context['no_films'] = Film.objects.all().count()
        return context
        

class FilmListView(ListView):
    template_name = 'home.html'
    model = Film
    context_object_name = 'films'
    
    def get_queryset(self, *args, **kwargs):
        return Film.objects.all()
    
    
class FilmDetailView(DetailView):
    template_name = 'film.html'
    model = Film
    context_object_name = 'film'
    
class ActorDetailView(DetailView):
    template_name = 'actor.html'
    model = Actor
    context_object_name = 'actor'
    
class DiscussionDetailView(DetailView):
    template_name = 'discussion.html'
    model = Discussion
    context_object_name = 'discussion'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

from django.http import HttpResponse
from django.shortcuts import render
from cinemadatabase.models import Film
def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		films = Film.objects.filter(name__icontains=q)	
		return render(request, 'search.html',    
			{'films': films})
	else :
	    return redirect('/')


# class TaskCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'form.html'
#     form_class = TaskForm
#     model = Task
    
#     def get_success_url(self, *args, **kwargs):
#         return reverse(
#             'task_detail', 
#             kwargs={
#                 'pk': self.object.pk
#             }
#         )


# class TaskUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'form.html'
#     form_class = TaskForm
#     model = Task
    
#     def get_success_url(self, *args, **kwargs):
#         return reverse(
#             'task_detail', 
#             kwargs={
#                 'pk': self.object.pk
#             }
#         )


# class TaskDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'delete.html'
#     model = Task
    
#     def get_success_url(self, *args, **kwargs):
#         return reverse(
#             'group_detail', 
#             kwargs={
#                 'pk': self.object.group.pk
#             }
#         )


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
                return redirect('film_list')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


class UserDetailView(DetailView):
    template_name = 'user.html'
    model = User
    context_object_name = 'user'

def category(request):
    object_list = Category.objects.all()
    context = {'object_list': object_list,}
    return render(request, 'category.html', context)