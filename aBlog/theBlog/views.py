from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from . forms import PostForm,CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


# list view puts all blog posts on our page
class homeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['publication_date']

# inside of this; query our category model and pull out names of categories then create links outta them
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(homeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = category_menu
        return context


# detail view - one blog post on a page
class articleView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(articleView, self).get_context_data(*args, **kwargs)

        # this will grab from our post table the post with id of the primary key we are currently on
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        Total_likes = stuff.total_likes()  # calling total_likes from our models.py

        Liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            Liked = True

        context["cat_menu"] = category_menu
        context["total_likes"] = Total_likes
        context["liked"] = Liked
        return context

# class addBlog(CreateView):
#     model = Post
#     template_name = "add_post.html"
#     fields = "__all__"


class addBlog(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class editBlog(UpdateView):
    model = Post
    form_class = PostForm
    # fields = ["title", "title_tag", "body"]
    template_name = "update_post.html"


class deleteBlog(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class addCategory(CreateView):
    model = Category
    fields = "__all__"
    template_name = "add_category.html"


def categoryView(request, cats):
    # replacing those dashes with a space
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(request, "categories.html", {"Cats": cats.title().replace("-", " "), "Category_posts": category_posts})


def categorylistView(request):
    category_menu_list = Category.objects.all()
    return render(request, "categories_list.html", {"Category_list": category_menu_list})


# when this gets called it means we've liked the post, that means we need to save that to the database - so we need to know which post we're talking about
# and save it as a like, we can do that using get object or 404.
# We wanna look up our post and we wanna grab the id that equals "" - this is a form being submitted and when we submit it we can grab sth from  that form by calling request.form.get and the calling the post_id
def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))

    Liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        Liked = False
    else:
        post.likes.add(request.user)
        Liked = True

    return HttpResponseRedirect(reverse("articles", args=[str(pk)]))


class addComment(CreateView):
    model = Comment
    form_class = CommentForm
    # fields = "__all__"
    template_name = "add_comments.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)
