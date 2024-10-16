# slideapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import delete_version
from .views import compare_versions

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_slide, name='create_slide'),
    path('edit/<int:slide_id>/', views.edit_slide, name='edit_slide'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('delete/<int:slide_id>/', views.delete_slide, name='delete_slide'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('toggle_lock/<int:slide_id>/', views.toggle_lock, name='toggle_lock'),
    path('public/', views.public_slides, name='public_slides'),
    path('public/edit/<int:slide_id>/', views.public_edit_slide, name='public_edit_slide'),
    path('slide/<int:slide_id>/history/', views.slide_history, name='slide_history'),
    path('slide/<int:slide_id>/history/', views.slide_history, name='slide_history'),
    path('slide/<int:slide_id>/restore_version/', views.restore_slide_version, name='restore_slide_version'),
    path('slide/<int:slide_id>/delete_version/', delete_version, name='delete_version'),
    path('slide/<int:slide_id>/compare_versions/', compare_versions, name='compare_versions'),
]