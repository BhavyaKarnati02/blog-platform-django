from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, Comment
from .forms import PostForm, CommentForm


def home(request):

    posts_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 3)

    page_number = request.GET.get('page')

    posts = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'posts': posts
    })


def search_posts(request):

    query = request.GET.get('q')

    posts_list = Post.objects.filter(
        title__icontains=query
    ).order_by('-created_at')

    paginator = Paginator(posts_list, 3)

    page_number = request.GET.get('page')

    posts = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'posts': posts
    })


@login_required
def create_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('home')

    else:

        form = PostForm()

    return render(request, 'create_post.html', {
        'form': form
    })


def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    comments = post.comment_set.all()

    if request.method == 'POST':

        if request.user.is_authenticated:

            form = CommentForm(request.POST)

            if form.is_valid():

                comment = form.save(commit=False)

                comment.post = post

                comment.user = request.user

                comment.save()

                return redirect('post_detail', post_id=post.id)

    else:

        form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def like_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if post.likes.filter(id=request.user.id).exists():

        post.likes.remove(request.user)

    else:

        post.likes.add(request.user)

    return redirect('post_detail', post_id=post.id)


@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:

        return redirect('home')

    if request.method == 'POST':

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect('post_detail', post_id=post.id)

    else:

        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {
        'form': form
    })


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.user == post.author:

        post.delete()

    return redirect('home')