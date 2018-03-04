from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.shortcuts import render, redirect
from django.views import View
from posts.forms import PostForm
from posts.models import Post


@login_required
def home(request):
    last_posts = Post.objects.all().filter(publish_date__lte=datetime.now()).order_by('-publish_date')
    return render(request, 'home_page.html', {'last_posts': last_posts})


class NewPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home_page')

        print(form.errors)
        return render(request, 'new_post.html', {'form': form})


@login_required
def blogsList(request):
    blogs_list = User.objects.all()
    return render(request, 'blogs_list.html', {'blogs_list': blogs_list})


@login_required
def blogDetail(request, user_name):
    user_post_list = Post.objects.filter(owner__username=user_name).filter(publish_date__lte=datetime.now()).order_by('-publish_date')
    return render(request, 'blog_detail.html', {'post_list': user_post_list})


@login_required
def postDetail(request, user_name, pk):
    post_detail = Post.objects.filter(owner__username=user_name, pk=pk)
    return render(request, 'post_detail.html', {'post': post_detail})
