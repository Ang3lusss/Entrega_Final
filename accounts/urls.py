# accounts/urls.py
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',  LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/editar/', views.profile_edit, name='profile_edit'),
    path(
        'password/change/',
        PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url=reverse_lazy('accounts:password_change_done')
        ),
        name='password_change',
    ),
    path('password/change/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), 
        name='password_change_done'),
]
