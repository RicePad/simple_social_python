from django.conf.urls import url
from posts import views

app_name="posts"

urlpatterns = [
    url(r"^$", views.PostListView.as_view(), name="all"),
    url(r"^$", views.CreatePostView.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",views.UserPostList.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetailView.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]
