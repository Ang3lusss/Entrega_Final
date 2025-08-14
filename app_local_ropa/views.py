from django.contrib import messages
from django.contrib.auth.decorators import login_required            # decorador (requisito)
from django.contrib.auth.mixins import LoginRequiredMixin            # mixin (requisito)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Prenda, Categoria
from .forms import PrendaForm

class PrendaListView(ListView):
    model = Prenda
    template_name = 'app_local_ropa/prenda_list.html'
    context_object_name = 'prendas'
    paginate_by = 8

    def get_queryset(self):
        qs = super().get_queryset()
        q   = self.request.GET.get('q', '')
        cat = self.request.GET.get('cat', '')
        order = self.request.GET.get('order', 'recientes')

        if q:
            qs = qs.filter(nombre__icontains=q) | qs.filter(color__icontains=q)
        if cat:
            qs = qs.filter(categoria__id=cat)

        if order == 'recientes':
            qs = qs.order_by('-fecha_publicacion')
        elif order == 'precio_asc':
            qs = qs.order_by('precio')
        elif order == 'precio_desc':
            qs = qs.order_by('-precio')

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        ctx['cat'] = self.request.GET.get('cat', '')
        ctx['order'] = self.request.GET.get('order', 'recientes')
        ctx['categorias'] = Categoria.objects.all()
        return ctx

class PrendaDetailView(DetailView):
    model = Prenda
    template_name = 'app_local_ropa/prenda_detail.html'
    context_object_name = 'prenda'

@login_required
def prenda_create(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prenda creada correctamente.')
            return redirect('app_local_ropa:prenda_list') 
    else:
        form = PrendaForm()
    return render(request, 'app_local_ropa/prenda_form.html', {'form': form, 'accion': 'Crear'})

class PrendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = PrendaForm
    template_name = 'app_local_ropa/prenda_form.html'
    success_url = reverse_lazy('app_local_ropa:prenda_list')  

class PrendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Prenda
    template_name = 'app_local_ropa/prenda_confirm_delete.html'
    success_url = reverse_lazy('app_local_ropa:prenda_list')  