from django.db import models

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_judul = models.CharField(max_length=250)
    article_isi = models.TextField()

