from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:id>/comment/', views.comment_create, name='comment_create'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('categories/', views.category_list, name='category_list'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),

    path('post/<int:id>/comment/', views.comment_create, name='comment_create'),
    
    path('categories/create/', views.category_create, name='category_create'),

]
