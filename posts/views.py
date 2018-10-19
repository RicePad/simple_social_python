from django.shortcuts import render

# Create your POST views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import CreateView, ListView, DetailView, DeleteView

from braces.views import SelectRelatedMixin

from . import forms
from posts.models import Post

from django.contrib.auth import get_user_model
User = get_user_model()


class PostListView(SelectRelatedMixin, ListView):
    model = Post
    select_related = ("user", "group")

class UserPostList(ListView):
    model = Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefect_related("posts").get(
            username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetailView(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ("user", "group")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__name__iexact=self.kwargs.get("username")
        )


class CreatePostView(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ("message", "group")
    model = Post


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.username
        self.object.save()
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
