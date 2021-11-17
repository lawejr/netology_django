from django.shortcuts import render
from django.db.models import Prefetch

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related(
        Prefetch('scopes', queryset=ArticleScope.objects.order_by('-is_main', 'tag'))
    )
    context = {
        'object_list': articles
    }

    return render(request, template, context)
