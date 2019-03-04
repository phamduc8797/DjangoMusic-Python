# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from .models import Singer, Song

after_logout = settings.LOGOUT_REDIRECT_URL

class HomeView(ListView):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        return render(request, "homes/home.html", {})

class LogoutView(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    next_page = after_logout

class ListSingerView(ListView):
    model = Singer       
    def get(self, request, *args, **kwargs):
        template_name = 'singers/list-singer.html'
        obj = {
            'listcontents': Singer.objects.all()
        }
        return render(request, template_name, obj)

class ListSongView(ListView):
    model = Song
    def get(self, request, *args, **kwargs):
        template_name = 'songs/list-songs.html'
        obj = {
            'songs': Song.objects.all()
        }
        return render(request, template_name, obj)

class DetailSongView(DetailView):
    model = Song
    template_name = 'songs/song_detail.html'
    def get_context_data(self, **kwargs):
        context = super(DetailSongView, self).get_context_data(**kwargs)
        return context
