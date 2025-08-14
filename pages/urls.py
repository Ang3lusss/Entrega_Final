from django.urls import path
from .views import (home, about, PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView)

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/crear/', PageCreateView.as_view(), name='page_form'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/borrar/', PageDeleteView.as_view(), name='page_delete'),
]
