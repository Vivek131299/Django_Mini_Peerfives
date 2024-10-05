from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_user_page, name="new_user_page"),
    path('create_new_user/', views.create_new_user, name="create_new_user"),
    path('<int:id>/', views.user_info_page, name="user_info_page"),
    path('<int:id>/p5', views.p5_balance_page, name="p5_balance_page"),
    path('<int:id>/rewards/new', views.new_reward_page, name="new_reward_page"),
    path('<int:id>/rewards/new/create', views.create_reward, name="create_reward"),
    path('<int:id>/rewards', views.reward_balance_page, name="reward_balance_page"),
    path('', views.get_all_users, name="get_all_users"),
]