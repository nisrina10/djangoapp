from django import forms

class TambahArtikel(forms.Form):
	#article_id = forms.AutoField(primary_key=True)
	article_judul = forms.CharField(label="Judul", max_length=200)
	article_isi = forms.CharField(widget=forms.Textarea)
