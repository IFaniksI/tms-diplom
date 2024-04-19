from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles_list': articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
