from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from .models import Page

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "estoque/index.html")
    
class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "estoque/form.html", {"form": form})
    
    def post(self, request):
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("estoque:index")
        return render(request, "estoque/form.html", {"form": form})

class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        lista = Page.objects.order_by("data")
        return render(request, "estoque/lista.html", {"lista": lista})
    
class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "estoque/detalhes.html", {"page": page})
    
class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render(request, "estoque/editar.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("estoque:detalhes", id=id)
        return render(request, "estoque/form.html", {"form": form})

class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "estoque/apagar.html", {"page": page})
    
    def post(self, request, id):
       page = get_object_or_404(Page, id=id)
       page.delete()
       return redirect('estoque:lista') 

index = IndexView.as_view()
criar_pagina = PageCreateView.as_view()
lista = PageListView.as_view()
detalhes = PageDetailView.as_view()
editar = PageUpdateView.as_view()
apagar = PageDeleteView.as_view()