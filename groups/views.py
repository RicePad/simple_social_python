from django.shortcuts import render
from django.contrib.auth.mixins import(LoginRequiredMixin,PermissionRequiredMixin)
from django.core.urlresolvers import reverse
from django.views.generic CreateView, ListView, DetailView
from groups.models Group, GroupMember
from groups import models

# Create your GROUP views here.

class CreateGroupView(LoginRequiredMixin, CreateView):
    fields = ("name", "description")
    model = Group

class SingleGroup(DetailView):
    model = Group

class ListGroups(ListView):
    model = Group
