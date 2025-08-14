from django.urls import path
from .views import (
    PrendaListView, PrendaDetailView,
    prenda_create, PrendaUpdateView, PrendaDeleteView
)

app_name = 'app_local_ropa'

urlpatterns = [
    path('', PrendaListView.as_view(), name='prenda_list'),
    path('crear/', prenda_create, name='prenda_create'),
    path('<int:pk>/', PrendaDetailView.as_view(), name='prenda_detail'),
    path('<int:pk>/editar/', PrendaUpdateView.as_view(), name='prenda_update'),
    path('<int:pk>/eliminar/', PrendaDeleteView.as_view(), name='prenda_delete'),
]
