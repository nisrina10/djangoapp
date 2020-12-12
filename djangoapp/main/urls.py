from django.urls import path
from . import views

urlpatterns = [	
	path('', views.home, name='home'),
	path('home/', views.home, name='home'),
	#path('tambah/', views.tambah, name='index'),
	path('list/', views.list, name='list'),
	path('<int:article_id>', views.index, name='index'),
]
