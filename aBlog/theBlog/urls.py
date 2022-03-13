from django.urls import path
from .views import homeView, articleView, addBlog, editBlog, deleteBlog, addCategory, categoryView, categorylistView, likeView, addComment

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('article/<int:pk>/', articleView.as_view(), name="articles"),
    path("add-blog/", addBlog.as_view(), name="addBlog"),
    path("add-category/", addCategory.as_view(), name="addCategory"),
    path("article/<int:pk>/update-blog", editBlog.as_view(), name="updateBlog"),
    path("article/<int:pk>/delete", deleteBlog.as_view(), name="deleteBlog"),
    path("category/<str:cats>", categoryView, name="category"),
    path("category-list", categorylistView, name="category-list"),
    path("like/<int:pk>", likeView, name="likePost"),
    path("article/<int:pk>/comment/", addComment.as_view(), name="comments"),
]
