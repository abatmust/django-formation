from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Article, Category
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class ListArticleView(ListView):
    # model = Article
    queryset = Article.objects.filter(state=1).order_by('-created')
    template_name = "blog/index.html"
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categories'] = Category.objects.all()
        return context

# class ListArticleView(View):
#     def get(self, request):
#         articles = Article.objects.filter(state=1)
#         categories = Category.objects.filter(state=1)
# # ----------------pagination-------------------------
#         item_per_page = 2
#         page = request.GET.get("page")
#         paginator = Paginator(articles, item_per_page)

#         try:
#             articles = paginator.page(page)
#         except PageNotAnInteger:
#             page = 1
#             articles = paginator.page(page)
#         except EmptyPage:
#             page = paginator.num_pages
#             articles = paginator.page(page)

#         context = {"articles": articles,
#                    "categories": categories}

#     # ---------------------------------------------------

#         return render(request, "blog/index.html", context)


def index(request):
    articles = Article.objects.filter(state=1)
    categories = Category.objects.filter(state=1)
# ----------------pagination-------------------------
    item_per_page = 2
    page = request.GET.get("page")
    paginator = Paginator(articles, item_per_page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        articles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        articles = paginator.page(page)

    context = {"articles": articles,
               "categories": categories}


# ---------------------------------------------------

    return render(request, "blog/index.html", context)


class ShowArticleView(DetailView):
    model = Article

    template_name = "blog/show.html"
    # class ShowArticleView(View):
    #     def get(self, request, slug):
    #         article = get_object_or_404(Article, slug=slug)

    #         return render(request, "blog/show.html", {"article": article})


def show(request, slug):

    # try:
    #     article = Article.objects.get(slug=slug)
    # except:
    #     raise Http404
    article = get_object_or_404(Article, slug=slug)

    return render(request, "blog/show.html", {"article": article})


class CreateArticleView(CreateView):
    model = Article
    # fields = '__all__'
    form_class = ArticleForm
    template_name = "blog/create.html"
    success_url = "/articles"

    def form_valid(self, form):
        # If the form is valid, save the associated model
        form.instance.state = 1
        form.save()
        return super().form_valid(form)

# class CreateArticleView(View):
#     def get(self, request):
#         form = ArticleForm
#         return render(request, "blog/create.html", {"form": form})

#     def post(self, request):
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("list_of_article")


@login_required(login_url="login")
def create(request):
    form = ArticleForm
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_of_article")
        else:
            messages.warning(
                request, 'there is a problem with data validity !')
    return render(request, "blog/create.html", {"form": form})


class EditArticleView(View):
    def get(self, request, id):
        article = Article.objects.get(pk=id)
        form = ArticleForm(instance=article)
        return render(request, "blog/edit.html", {"form": form})

    def post(self, request, id):
        article = Article.objects.get(pk=id)
        form = ArticleForm(data=request.POST,
                           instance=article, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_of_article")


def edit(request, id):

    article = Article.objects.get(pk=id)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("list_of_article")
    else:
        form = ArticleForm(instance=article)
    return render(request, "blog/edit.html", {"form": form})


def delete(request, id):
    article = Article.objects.get(pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect("list_of_article")
