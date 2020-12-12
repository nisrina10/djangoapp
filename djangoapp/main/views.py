from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import TambahArtikel
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(response, article_id):
	da = Article.objects.get(article_id=article_id)
	return render(response, "main/list.html", {"da":da})

@login_required(login_url='/login')
def list(request):
	
	search_post = request.GET.get('search')
	if search_post:
		daftar = Article.objects.filter(Q(article_judul__icontains=search_post) & Q(article_isi__icontains=search_post))
	else:
		daftar = Article.objects.all()
	
	return render(request, "main/list.html", {"daftar":daftar})

def home(response):
	return render(response, "main/home.html", {})

# def search(request):


def tambah(request):
	form = TambahArtikel()
	return render(request, "main/tambah.html", {"form": form})

    
