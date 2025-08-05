from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup/', views.signup, name='signup'),
    path('post/new/', views.post_new, name='post_new'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'), 
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('category/<str:category_name>/', views.category_post_list, name='category_post_list'),
    path('search/', views.search_results, name='search_results'), 

]