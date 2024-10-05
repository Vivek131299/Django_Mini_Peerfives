from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_user_page, name="new_user_page"),
    path('create_new_user/', views.create_new_user, name="create_new_user"),
    path('<int:id>/', views.user_info_page, name="user_info_page"),
    path('', views.get_all_users, name="get_all_users"),
]