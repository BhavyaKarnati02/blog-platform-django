from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment

from .forms import PostForm, CommentForm


def home(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'posts': posts})


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

    return render(request, 'create_post.html', {'form': form})


def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.post = post

            comment.user = request.user

            comment.save()

            return redirect('post_detail', post_id=post.id)

    else:

        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'post_detail.html', context)