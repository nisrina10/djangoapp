from django.shortcuts import render, redirect
from .forms import FormRegistrasi

def register(response):
	if response.method == "POST":
		form = FormRegistrasi(response.POST)
		if form.is_valid():
	 		form.save()	
	 		return redirect('/home')
	else:
		form = FormRegistrasi()

	return render(response, "akun/register.html", {"form":form})

