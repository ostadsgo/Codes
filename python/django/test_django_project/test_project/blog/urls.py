from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
