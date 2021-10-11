import urllib.parse

from customers.decorators import customer_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Category, Comment, Post


@customer_required
def blog_post_view(request):
    '''
    This view will render all posts & filter categories. 
    '''
    posts = Post.published.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    category = request.GET.get('category')
    if category == None:
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
        context = {
            'post': post,
            'comments': comments,
            'total_category': total_category,
            'share_able_link': share_able_link,
            'total_comments_on_post': total_comments,
            'category': category.values_list('name', flat=True).first(),
        }

        return render(request, 'blog/blog_detail.html', context)

# def blog_search_view(request):
#     '''
#     This view will search for the specific blog post.
#     '''
#     query = request.GET.get('q')
#     if query:
#         posts = Post.published.filter(title__icontains=query)
#         context = {
#             'query': query,
#             'posts': posts,
#         }
#         return render(request, 'blog/blog_search.html', context)
#     else:
#         return redirect('blog:blog_post')

# @customer_required
# def comment_delete_view(request, slug, pk):
#     '''
#     This will delete the comment.
#     '''
#     comment = get_object_or_404(Comment, pk=pk)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('blog:blog_detail', slug=slug)
