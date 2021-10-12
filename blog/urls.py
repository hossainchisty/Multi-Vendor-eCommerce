from django.urls import path
from . views import blog_post_view, blog_details_view, create_comment_view, blog_search_view

app_name = 'blog'

urlpatterns = [
    path('', blog_post_view, name='blog_view'),
    path('<slug:slug>', blog_details_view, name='blog_detail'),
    path('<slug:slug>/', create_comment_view, name='create_comment'),
    path('search/', blog_search_view, name='search'),
    # path('<slug:slug>/<int:pk>/delete', comment_delete_view, name='comment_delete'),
]
