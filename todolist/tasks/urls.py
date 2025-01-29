from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('tasks/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),  # Task creation view
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('done/<int:task_id>/', views.mark_done, name='mark_done'),  # Mark task as done
     path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task view
    path('logout/', views.logout_user, name='logout'),

]
