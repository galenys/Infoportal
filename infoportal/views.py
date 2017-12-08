# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.urls import reverse

from django.utils import timezone

from .models import Post, PostForm, User

# Create your views here.
def index(request):
    all_posts = Post.objects.order_by('-pub_date')
    # class_names = []
    # for x in range(0,len(all_posts))
    #     class_names[x] = all_posts[x].
    context = {
        "all_posts": all_posts
    }
    return render(request, 'infoportal/index.html', context)
def myposts(request):
    context = {
    }
    return render(request, 'infoportal/myposts.html', context)
def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect("infoportal:index")
    else:
        form = PostForm()
        context = {
            "form": form
        }
        return render(request, 'infoportal/newpost.html', context)
