import urllib.parse

from customers.decorators import customer_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import CommentForm
from .models import Category, Comment, Post


@customer_required
@cache_page(60 * 2)
def blog_post_view(request):
    '''
    This view will render all posts & filter categories.
    '''
    posts = Post.published.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    category = request.GET.get('category')
    if category is None:
        posts = Post.published.all()
    else:
        posts = Post.published.filter(category__name=category)

    category = Category.objects.all()
    context = {
        'categories': category,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blog.html', context)


@customer_required
@cache_page(60 * 2)
def blog_details_view(request, slug):
    '''
    This blog details will show more info about a specific blog post.
    '''
    post = get_object_or_404(Post, slug=slug)
    '''
    This will decode the post title for share article link.
    '''
    share_able_link = urllib.parse.quote(post.title)
    '''
    This will display the total comments of specific post.
    '''
    total_comments = Comment.objects.filter(post=post).count()
    '''
    This will display the total category number of the post.
    '''
    total_category = Category.objects.filter(post=post).count()
    '''
    This will display specific category of the post.
    '''
    category = Category.objects.filter(post=post)
    '''
    This will display who commented on the post.
    '''
    comments = Comment.objects.filter(post=post, customer=request.user.customer)

    context = {
        'post': post,
        'comments': comments,
        'total_category': total_category,
        'share_able_link': share_able_link,
        'total_comments_on_post': total_comments,
        'category': category.values_list('name', flat=True).first(),
    }

    return render(request, 'blog/blog_detail.html', context)


@customer_required
def create_comment_view(request, slug):
    '''
    This will create new comment on a specific post.
    '''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, slug=slug)
            comment.customer = request.user.customer
            comment.body = request.POST.get('body')
            comment.save()
            return redirect('blog:blog_detail', slug=slug)
    else:
        return render(request, 'blog/blog_detail.html')


@customer_required
def blog_search_view(request):
    '''
    This view will search for the blog post with title, slug and category.
    '''
    queryset = request.GET.get('q')
    if queryset:
        posts = Post.published.filter(Q(title__icontains=queryset) | Q(slug__icontains=queryset) | Q(category__name=queryset))
        context = {
            'query': queryset,
            'page_obj': posts,
        }
        return render(request, 'blog/blog.html', context)
    else:
        raise Http404


# @customer_required
# def comment_delete_view(request, slug, pk):
#     '''
#     This will delete the comment.
#     '''
#     comment = get_object_or_404(Comment, pk=pk)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('blog:blog_detail', slug=slug)
