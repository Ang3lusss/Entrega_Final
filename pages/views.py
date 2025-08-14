from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    ordering = ['-fecha_publicacion']

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'bajada', 'cuerpo', 'imagen']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')
    login_url = 'accounts:login'
    def form_valid(self, form):
        messages.success(self.request, 'Página creada correctamente.')
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['titulo', 'bajada', 'cuerpo', 'imagen']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')
    login_url = 'accounts:login'
    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada.')
        return super().form_valid(form)

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')
    login_url = 'accounts:login'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Página eliminada.')
        return super().delete(request, *args, **kwargs)
