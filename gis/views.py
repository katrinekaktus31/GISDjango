from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from gis.models import Article


def home(request):
    # return HttpResponse("Hello world!")
    # return render(request, "gis/home.html")
    articles = Article.objects.all()
    # add all object from data base (models.py)
    context = {
        'articles': articles
    }
    return render(request, "gis/home.html", context)


# generated for this request some templates
def about(request):
    return render(request, "gis/about.html")


def show_articles(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'gis/article.html', {'article': article})

